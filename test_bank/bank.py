def main():
    print(value("hello"))

def value(greet):

    greet = greet.lower()
    greet = greet.strip()

    if greet.startswith("hello"):
        x="$100"
    elif greet.startswith("h"):
        x="$20"
    else:
        x="$0"
    return x

if __name__ == "__main__":
    main()
