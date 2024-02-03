
input_date = input("Date: ")
month,day,year = input_date.split('/')

month = int(month)
day = int(day)

print(f"Month::{month:02}")
print(f"Day::{day:02}")
print(f"Year::{year:02}")
