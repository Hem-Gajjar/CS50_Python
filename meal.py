def main():
    str= input("What time is it? ")
    num = convert(str)

    if 7 <= num <= 8:
        print("breakfast time")
    elif 12 <= num <= 13:
        print("lunch time")
    elif 18 <= num <= 19:
        print("dinner time")

def convert(time):
    h,m = time.split(":")
    m = int(m)/60
    x = int(h)+m
    return x


if __name__ == "__main__":
    main()
