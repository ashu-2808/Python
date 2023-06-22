#Finding factorial of a given number using for loop in python
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
num=int(input("Enter num for factorial:"))
print("The factorial of",num,"is:",factorial(num))