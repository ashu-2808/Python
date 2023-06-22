#PALINDROME USING STRING SLICING
x=input("Enter any string or num:")
y=(x[::-1])
if x.upper()==y.upper():
    print("Palindrome")
else:
    print("Not Palindrome")

#PALINDROME USING WHILE LOOP INSIDE A FUNCTION
def isPalindrome(s):
    rev=0
    x=len(str(s))
    while(s!=0):
        r=s%10
        rev=(rev*10) +r
        s=s//10
    return rev
num=int(input("Enter any integer:"))
ans=isPalindrome(num)
if num==ans:
    print("Palindrome")
else:
    print("Not Palindrome")


