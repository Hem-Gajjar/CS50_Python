
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

while True:
    input_date = input("Date: ")
    try:
        month,day,year = input_date.split('/')
        year = int(year)
        month = int(month)
        day = int(day)
        if(month >= 1 and month <= 12 and day >=1 and day <= 31):
            print(f"{year:02}-{month:02}-{day:02}")
            break
        else:
            continue

    except ValueError:
        month,day_year = input_date.split(' ',maxsplit=1)
        day,year = day_year.split(',')
        
        year = int(year)
        day = int(day)
        month = month_list.index(month)+1
        if(day >=1 and day <= 31 ):
            print(f"{year:02}-{month:02}-{day:02}")
            break
        else:
            continue












# try:
#     month,day,year = input_date.split('/')
#     month = int(month)
#     day = int(day)
#     print(f"{year:02}-{month:02}-{day:02}")
# except ValueError:
#     month,day_year = input_date.split(' ',maxsplit=1)
#     day,year = day_year.split(',')
#     year = int(year)
#     day = int(day)
#     month = month_list.index(month)+1
#     print(f"{year:02}-{month:02}-{day:02}")


