class DeliveryOption:
    def __init__(self, name, cost, time):
        self.name = name
        self.cost = cost
        self.time = time

    def compute_utility(self, weight_time, weight_cost):
        return weight_time * (1 / self.time) + weight_cost * (1 / self.cost)


class ShoppingAssistant:
    def __init__(self, customer_name, weight_time=0.6, weight_cost=0.4):
        self.customer_name = customer_name
        self.weight_time = weight_time
        self.weight_cost = weight_cost
        self.options = []

    def add_option(self, delivery_option):
        self.options.append(delivery_option)

    def recommend(self):
        utilities = {}
        for option in self.options:
            utility = option.compute_utility(self.weight_time, self.weight_cost)
            utilities[option.name] = utility
            print(f"Utility of {option.name}: {utility:.3f}")
        best_option = max(utilities, key=utilities.get)
        print(f"\nRecommended delivery option for {self.customer_name}: {best_option}")


option_a = DeliveryOption("Option A", cost=20, time=2)
option_b = DeliveryOption("Option B", cost=10, time=5)

assistant = ShoppingAssistant(customer_name="Alice", weight_time=0.7, weight_cost=0.3)
assistant.add_option(option_a)
assistant.add_option(option_b)
assistant.recommend()
