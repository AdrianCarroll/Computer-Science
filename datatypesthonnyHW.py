temp=float(input("Enter the average temberature of today "))
temp2=float(input("Enter the average temberature of yesterday "))
temp3=float(input("Enter the average temberature of two days ago "))
temp4=float(input("Enter the average temberature of three days ago "))
temp5=float(input("Enter the average temberature of four days ago "))
temp6=float(input("Enter the average temberature of five days ago "))
temp7=float(input("Enter the average temberature of six days ago "))
print("The average temperature for next week will be", (temp+temp2+temp3+temp4+temp5+temp6+temp7)/2 )

ex=float(input("Enter a value for X " ))
why=float(input("Enter a value for Y " ))
zed=float(input("Enter a value for Z " ))
PI=3.14
print(4*ex**4+3*why**3+9*zed+6*PI)

sec=60
time=int(input("Enter a number of seconds"))
mins=time//sec
print("Total time is", mins)

hour=float(input("Enter a number between 1-12: " ))
clock=float(input("What time is it?: " ))
oclock=clock+hour
if oclock>12:
    lock=oclock-12
    print("It will be", lock, "o'clock")
else:
    print("It will be", oclock, "o'clock")

xyz=int(input("Enter a three digit number: " ))
xyz2=xyz%10
xyz3=xyz//10
xyz4=xyz3%10
xyz5=xyz3//10
print("Your number reversed is", xyz2, xyz4, xyz5, sep='')

day=1
month=30*day
year=12*month
dateday=int(input("Enter a day: " ))
datemonth=int(input("Enter a month as a number: " ))
date=0+dateday*day+datemonth*month
print("It is the", date, "day of the year")