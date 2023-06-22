#Checking for armstrong num using while loop inside a function
def isArmstrong(n):
    arm=0
    x=len(str(n))
    while(n!=0):
        r=n%10
        arm=arm+(r**x)
        n=n//10
    return arm
num=int(input("Enter any num:"))
ans=isArmstrong(num)
if num==ans:
    print("Armstrong")
else:
    print("Not Armstrong")