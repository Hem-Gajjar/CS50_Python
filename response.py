from validator_collection import validators

def main():
    myemail = input("What's your email address?")
    try:
        isvalid= validators.email(myemail)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
