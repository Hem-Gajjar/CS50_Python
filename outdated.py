
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
# while True:
try:
    input_date = input("Date: ")
    month,day,year = input_date.split('/')
    month = int(month)
    day = int(day)
    print(f"{year:02}-{month:02}-{day:02}")
except ValueError:
    month = month_list.index(month)
    print(month)



# if(type(month) == int):

# else:

