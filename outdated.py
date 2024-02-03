
# month_list = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

input_date = input("Date: ")
month,day,year = input_date.split('/')

month = int(month)
day = int(day)

print(f"Month::{month:02}")
print(f"Day::{day:02}")
print(f"Year::{year:02}")
