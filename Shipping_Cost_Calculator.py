# Shipping Cost Calculator
## Input package weight and shipping rate
try:
    weight = float(input("Enter the package weight in kilograms: "))
    if weight < 0:
        raise ValueError("Weight cannot be negative")
except ValueError as e:
    print(f"Invalid weight input: {e}")
    exit(1)

try:
    rate = float(input("Enter the shipping rate per kilogram: "))
    if rate < 0:
        raise ValueError("Rate cannot be negative")
except ValueError as e:
    print(f"Invalid rate input: {e}")
    exit(1)
## Calculate shipping cost
shipping_cost = weight * rate
## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
