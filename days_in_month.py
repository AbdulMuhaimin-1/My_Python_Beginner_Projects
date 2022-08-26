# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(entered_year, entered_month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   year_check = is_leap(entered_year)
#   if year_check == True:
#     month_days[1] = 29
#   month_check = month_days[entered_month - 1]
#   return month_check

  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)



def hello(greet):
    greeting = f"hello {greet}"
    return greeting


print(hello("Haimin"))


