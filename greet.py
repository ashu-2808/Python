#Extracting system Time using time module of python and GREETING using Conditional Statements


import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestampH=int(time.strftime('%H'))
print(timestampH) #Only prints Hour
timestampM=time.strftime('%M') #Minute
timestampS=time.strftime('%S') #Second
print(timestampH,timestampM,timestampS)

#GREETING
if timestampH>0 and timestampH<12:
    print("Good Morning!!")
elif timestampH>=12 and timestampH<17:
    print("Good Afternoon!!")
elif timestampH>=17 and timestampH<20:
    print("Good Evening!!")
else:
    print("Good Night!!")