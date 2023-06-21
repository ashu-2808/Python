# Python program to convert temperatures to and from Celsius and Fahrenheit.

temp=input("Enter temperature in C or F(Like 32C or 100F:")
degree=int(temp[:-1])
unit=(temp[len(temp)-1:])

if unit.upper()=="C":
    result = (9 * degree) / 5 + 32
    aft="F"
elif unit.upper()=="F":
    result = (degree - 32) * 5 / 9
    aft="C"
else:
    print("Invalid Unit")
print("The temperature",temp,"in",aft,"is",result,"degrees")