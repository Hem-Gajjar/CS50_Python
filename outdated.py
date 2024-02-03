
month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

input_date = input("Date: ")
month,day,year = input_date.split('/')




if(type(month) == int):
    month = int(month)
    day = int(day)
    print(f"{year:02}-{month:02}-{day:02}")
else:
