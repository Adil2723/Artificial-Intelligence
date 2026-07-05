import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Load dataset
df = pd.read_csv("bank_data.csv")

# ---------------------- EDA ----------------------
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary:\n", df.describe())

# Drop duplicates
df.drop_duplicates(inplace=True)

# ---------------------- Data Cleaning ----------------------
# Convert date_of_birth to age
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
df['age'] = (pd.Timestamp.now() - df['date_of_birth']).dt.days // 365
df.drop(columns=['date_of_birth'], inplace=True)

# Drop irrelevant columns
df.drop(columns=['user_id', 'address', 'email'], inplace=True, errors='ignore')

# Handle missing values
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

# ---------------------- Encoding ----------------------
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# ---------------------- Scaling ----------------------
scaler = StandardScaler()
num_cols = df.drop(columns=['Approved', 'Approved_loan_amount']).columns
df[num_cols] = scaler.fit_transform(df[num_cols])

# ---------------------- Visualization ----------------------
sns.countplot(x='Approved', data=df)
plt.title("Loan Approval Distribution")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# ---------------------- Split Data ----------------------
X = df.drop(columns=['Approved', 'Approved_loan_amount'])
y_class = df['Approved']
y_reg = df['Approved_loan_amount']

X_train, X_test, y_train_c, y_test_c = train_test_split(X, y_class, test_size=0.2, random_state=42)
_, _, y_train_r, y_test_r = train_test_split(X, y_reg, test_size=0.2, random_state=42)

# ---------------------- Classification Model ----------------------
clf = RandomForestClassifier()
clf.fit(X_train, y_train_c)

y_pred_c = clf.predict(X_test)

print("\n--- Classification Report ---")
print("Accuracy:", accuracy_score(y_test_c, y_pred_c))
print(classification_report(y_test_c, y_pred_c))

cm = confusion_matrix(y_test_c, y_pred_c)
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.show()

# ---------------------- Regression Model ----------------------
reg = RandomForestRegressor()
reg.fit(X_train, y_train_r)

y_pred_r = reg.predict(X_test)

print("\n--- Regression Report ---")
print("MSE:", mean_squared_error(y_test_r, y_pred_r))
print("R2 Score:", r2_score(y_test_r, y_pred_r))

# ---------------------- Balancing Dataset ----------------------
approved = df[df['Approved'] == 1].sample(500, random_state=42)
rejected = df[df['Approved'] == 0].sample(500, random_state=42)

balanced_df = pd.concat([approved, rejected])

X_bal = balanced_df.drop(columns=['Approved', 'Approved_loan_amount'])
y_bal = balanced_df['Approved']

X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(X_bal, y_bal, test_size=0.2, random_state=42)

clf_bal = RandomForestClassifier()
clf_bal.fit(X_train_b, y_train_b)

y_pred_b = clf_bal.predict(X_test_b)

print("\n--- Balanced Dataset Results ---")
print("Accuracy:", accuracy_score(y_test_b, y_pred_b))
print(classification_report(y_test_b, y_pred_b))

cm_bal = confusion_matrix(y_test_b, y_pred_b)
sns.heatmap(cm_bal, annot=True, fmt='d')
plt.title("Balanced Confusion Matrix")
plt.show()
