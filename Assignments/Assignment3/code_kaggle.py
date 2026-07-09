import pandas as pd
import numpy as np
import warnings
import os

warnings.filterwarnings('ignore')

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

train_path = os.path.join(BASE_DIR, "train.csv")
test_path = os.path.join(BASE_DIR, "test.csv")

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

TARGET = 'Irrigation_Need'

cat_cols = [
    'Soil_Type','Crop_Type','Crop_Growth_Stage','Season',
    'Irrigation_Type','Water_Source','Mulching_Used','Region'
]

def engineer(df):
    d = df.copy()

    for c in cat_cols:
        d[c] = d[c].astype('category').cat.codes

    d['moisture_rain_ratio'] = d['Soil_Moisture'] / (d['Rainfall_mm'] + 0.01)
    d['heat_humidity'] = d['Temperature_C'] * d['Humidity']
    d['water_stress_idx'] = d['Temperature_C'] / (d['Soil_Moisture'] + 0.01)
    d['prev_irr_density'] = d['Previous_Irrigation_mm'] / (d['Field_Area_hectare'] + 0.1)
    d['sunlight_temp'] = d['Sunlight_Hours'] * d['Temperature_C']
    d['pH_moisture'] = d['Soil_pH'] * d['Soil_Moisture']

    return d.drop(columns=['id', TARGET], errors='ignore')

X_train_df = engineer(train)
X_test_df = engineer(test)

le = LabelEncoder()
y = le.fit_transform(train[TARGET])

scaler = StandardScaler()
X = scaler.fit_transform(X_train_df.values.astype('float32'))
X_test = scaler.transform(X_test_df.values.astype('float32'))

rng = np.random.RandomState(42)
idx = []

for cls in np.unique(y):
    cls_idx = np.where(y == cls)[0]
    n = int(len(cls_idx) * 0.2)
    idx.extend(rng.choice(cls_idx, n, replace=False))

idx = np.array(idx)

X_cv = X[idx]
y_cv = y[idx]

models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=12, min_samples_leaf=10,
                                            class_weight='balanced', random_state=42),

    "Logistic Regression": LogisticRegression(max_iter=300,
                                              class_weight='balanced', random_state=42),

    "Naive Bayes": GaussianNB(),

    "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=15,
                                           min_samples_leaf=5,
                                           class_weight='balanced',
                                           random_state=42, n_jobs=-1),

    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100,
                                                   learning_rate=0.1,
                                                   max_depth=5,
                                                   random_state=42)
}

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

cv_results = {}

for name, model in models.items():
    scores = cross_val_score(model, X_cv, y_cv,
                             cv=skf,
                             scoring='balanced_accuracy',
                             n_jobs=-1)
    cv_results[name] = scores

best_name = max(cv_results, key=lambda k: np.mean(cv_results[k]))
best_model = models[best_name]

best_model.fit(X, y)

preds = best_model.predict(X_test)
labels = le.inverse_transform(preds)

id_col = 'id' if 'id' in test.columns else test.columns[0]

submission = pd.DataFrame({
    id_col: test[id_col],
    TARGET: labels
})

output_path = os.path.join(BASE_DIR, "submission.csv")
submission.to_csv(output_path, index=False)

print("BEST MODEL:", best_name)
print("Submission saved at:", output_path)
