# This program checks to see if a year is a leap year.

print("Welcome to my Leap Year Checker!!!")

year = int(input("Please enter a year: "))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:

    print("leap year")

elif year % 4 == 0 and (year % 100) != 0:

    print("leap year")

else:

    print("not leap year")