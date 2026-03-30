hour = int(input("Enter current hour (0-23): "))

subtotal = 3000

if hour >= 6 and hour < 12:
    print("Morning discount")
    discount = subtotal * 0.10

elif hour >= 12 and hour < 17:
    print("No discount")
    discount = 0

elif hour >= 17 and hour < 22:
    print("Evening discount")
    discount = subtotal * 0.05

else:
    print("Closed")
    discount = 0

total = subtotal - discount
tip = total * 0.10
final = total + tip

print("Discount:", discount, "KZT")
print("Tip:", tip, "KZT")
print("Total:", final, "KZT")