#SIMPLE CALCULATOR USING MATCHCASE IN PYTHON(3.10 or above)

x=float(input("Enter 1st num:"))
y=float(input("Enter 2nd num:"))
print("Operations\nSUM: +\nSUB: -\nMul: *\nDiv: /\nMod: %")
z=input("Enter operation to be done:")
match z:
    case '+':
        print(x+y)       #no need of break statement
    case '-':
        print(x-y)
    case '*':
        print(x*y)
    case '/':
        if y==0:
            print("Denominator can't be 0")
        else:
            print(x/y)
    case '%':
        if y==0:
            print("Denominator can't be 0")
        else:
            print(x%y)
    case _:                 #Works same as default in C/Cpp/Java
        print("Invalid operation")