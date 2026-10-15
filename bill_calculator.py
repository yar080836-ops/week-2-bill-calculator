
# Week 2 Assignment: Simple Bill Calculator

# Ask the user for the price and quantity
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

# Calculate the total cost
total = price * quantity

# Display the bill summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
