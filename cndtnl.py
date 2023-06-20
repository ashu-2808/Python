# Python code for calculating percentage ,CGPA and Division obtained using Conditional Statements.

eng=int(input("Enter marks obtained in English:"))
mth=int(input("Enter marks obtained in Maths:"))
sci=int(input("Enter marks obtained in Science:"))
sst=int(input("Enter marks obtained in Social Studies:"))
ip=int(input("Enter marks obtained in Computer:"))
total=eng+mth+sci+sst+ip
print("Total marks obtained out of 500:",total)
perc=(total/500)*100
print("Percentage Obtained:",perc)
print("CGPA:",perc/9.5)
if perc>=60:
    print("1st Division")
elif perc>=50 and perc<60:
    print("2nd Division")
elif perc>=40 and perc<50:
    print("3rd Division")
else:
    print("FAIL") 
