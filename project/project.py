import csv
import re
def main():
    while(1):
        choice = 0
        choice = int(input(f"Select Choice\n(1) Select Movie By Year\n(2) Select Movie By Genre\n(3) Select Movie By Actor\n(4) Select Movie By Director\n(5) Exit\nEnter Choice::"))
        match choice:
            case 1:
                select_by_year()

            case 2:
                select_by_genre()

            case 3:
                select_by_actor()

            case 4:
                select_by_director()

            case 5:
                break

            case _:
                print("Invalid Choice")


def select_by_year():
    year = int(input("Enter the year::"))
    flag = 0
    with open("movies.csv","r") as csvfile:
        reader =csv.DictReader(csvfile)
        print(f"All movies released in year {year}")
        for row in reader:
            if(int(row["releaseYear"]) == year):
                flag = 1
                print(row["title"])

    if flag == 0:
        print(f"We are sorry there are no movies in year {year} in our dataset")

def select_by_genre():
    genre = input("Enter the genre to search::").capitalize()
    flag = 0
    with open("movies.csv","r") as csvfile:
        reader =csv.DictReader(csvfile)
        print(f"All movies of {genre} genre")
        for row in reader:
            if(re.search(f".*{genre}.*",row["genre"])):
                print(row["title"] + f"({row['genre']})")

def select_by_actor():
    print("Actor")

def select_by_director():
    print("Director")




if __name__ == "__main__":
    main()
