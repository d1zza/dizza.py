name = input("Enter customer name: ")

print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))

if name[0].upper() == "A" or name[0].upper() == "S":
    print("VIP customer")
else:
    print("Regular customer")