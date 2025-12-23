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

# Validate the calculated cost
if shipping_cost == 0:
    print("Warning: Calculated shipping cost is $0.00")
elif shipping_cost < 0:
    print("Error: Negative shipping cost calculated")
    exit(1)
## Display the result
print(f"Shipping Cost: ${shipping_cost:.2f} USD")
