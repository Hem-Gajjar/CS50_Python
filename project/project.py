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
    count = 1
    with open("movies.csv","r") as csvfile:
        reader =csv.DictReader(csvfile)
        print(f"All movies released in year {year}")
        for row in reader:
            if(int(row["releaseYear"]) == year):
                flag = 1
                print(row["title"])
                count += 1

    if flag == 0:
        print(f"We are sorry there are no movies in year {year} in our dataset")

def select_by_genre():
    genre = input("Enter the genre to search::").capitalize()
    flag = 0
    count = 1
    with open("movies.csv","r") as csvfile:
        reader =csv.DictReader(csvfile)
        print(f"All movies of {genre} genre")
        for row in reader:
            flag = 1
            if(re.search(f".*{genre}.*",row["genre"],re.IGNORECASE)):  # Here I have used regular expression to find if the specified genre exist in the string
                print(f"{count}. "+row["title"] + f"({row['genre']})")
                count += 1

    if flag == 0:
        print(f"We are sorry there are no movies of genre {genre} in our dataset")

def select_by_actor():
    actor = input("Enter the actor::").capitalize()
    flag = 0
    count = 1
    with open("movies.csv","r") as csvfile:
        reader =csv.DictReader(csvfile)
        print(f"All movies of {actor} actor")
        for row in reader:
            flag = 1
            if(re.search(f".*{actor}.*",row["actors"],re.IGNORECASE)):  # Here I have used regular expression to find if the specified actor exist in the string
                print(f"{count}. "+row["title"] + f"({row['actors']})")
                count += 1

    if flag == 0:
        print(f"We are sorry there are no movies of actor {actor} in our dataset")

def select_by_director():
    director = input("Enter the director::").capitalize()
    flag = 0
    count = 1
    with open("movies.csv","r") as csvfile:
        reader =csv.DictReader(csvfile)
        print(f"All movies of {director} director")
        for row in reader:
            flag = 1
            if(re.search(f".*{director}.*",row["directors"],re.IGNORECASE)):  # Here I have used regular expression to find if the specified director exist in the string
                print(f"{count}. "+row["title"] + f"({row['directors']})")
                count += 1

    if flag == 0:
        print(f"We are sorry there are no movies of director {director} in our dataset")





if __name__ == "__main__":
    main()
