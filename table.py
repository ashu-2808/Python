#Multiplication Table using python for and while loop

x=int(input("Enter number for multiplication table:"))
print("Using for loop")
for i in range(1,11):
    tb="{} x {} = {}"
    print(tb.format(x,i,x*i))

print("Using while loop")
j=1
while(j<11):
    tb="{} x {} = {}"
    print(tb.format(x,j,x*j))
    j=j+1

