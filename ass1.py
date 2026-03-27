customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input('Enter price per unit: '))
quantity = float(input("Enter quantity: "))
quant = str(quantity)


subtotal = price * quantity
discount = subtotal/10
total = subtotal - discount

sbt = str(subtotal)
disc = str(discount)
tot = str(total)



print('=' * 30)
print("          SHOP RECEIPT         ")
print('=' * 30)
print("Customer: " + customer)
print("Product: " + product)
print("Quantity: " + quant)
print("-" * 30)
print("Subtotal: " + sbt)
print("Discount " + disc)
print("Total: " + tot)
print("=" * 30)