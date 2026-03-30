name = input("Enter customer name: ")

total = 0
count = 0

item = input("Enter item name (or 'done' to finish): ")

while item != "done":
    price = int(input("Enter price: "))
    
    total = total + price
    count = count + 1

    item = input("Enter item name (or 'done' to finish): ")

print()
print("Customer:", name.upper())
print("Items:", count)
print("Subtotal:", total, "KZT")