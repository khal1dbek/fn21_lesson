# # Hometask 1
#
# import datetime
# import time
# import calendar
#
# d1 = "2024-06-14"
# date = datetime.datetime.strptime(d1, "%Y-%m-%d")
# t = time.strftime("%H:%M:%S")
#
# weekday_number = date.isoweekday()
# print(f"Current Date: {d1}, hour: {t}, the number of weekday: {weekday_number}")
#
# #Hometask 2
#
#
# year = 2024
# month = 7
#
# print("calendar for 1 month:")
# print(calendar.month(year, month))
# print("Calendar of yearly:")
# print(calendar.calendar(year))
#
#
# #Hometask 3
#
# from datetime import datetime
#
# def big_date(d1, d2):
#
#     date1 = datetime.strptime(d1, "%Y-%m-%d")
#     date2 = datetime.strptime(d2, "%Y-%m-%d")
#
#
#     if date1 > date2:
#         return d1
#     else:
#         return d2
#
# date1 = "2024-06-12"
# date2 = "2022-03-21"
#
# print("The biggest day:", big_date(date1, date2))
#
# # 2-usul
#
#
# a = int(input("Enter the date:"))
# b = int(input("Enter the date:"))
# if 0<a<31 and 0<b<31:
#     if a>b:
#       print(a, "This date is big")
#     if b>a:
#       print(b, "This date is big")
# else:
#     print("There is not this kind of date")
#
# # Hometask 4
#
# # import time
#
# current_time = time.localtime()
#
# formatted_date_time = time.strftime("%A %d %B %Y %H:%M:%S", current_time)
# formatted_date = time.strftime("%d.%m.%Y", current_time)
#
# print("Today:")
# print(formatted_date_time)
# print(formatted_date)
#

