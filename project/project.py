import csv
import re
import os
class Movie():
    def __init__(self,imdb_id,title,release_year,release_date,genre,writers,actors,directors,sequel,hitflop):
        self.imdb_id = imdb_id
        self.title = title
        self.release_year = release_year
        self.release_date = release_date
        self.genre = genre
        self.writers = writers
        self.actors = actors
        self.directors = directors
        self.sequel = sequel
        self.hitflop = hitflop

    #Here I have used Instance Method
    def addmymovie(self):
        myfile = open("movies.csv","a")
        mystring = str(
            f"\""+self.imdb_id+f"\","
            f"\""+self.title+f"\","
            f"\""+self.release_year+f"\","
            f"\""+self.release_date+f"\","
            f"\""+self.genre+f"\","
            f"\""+self.writers+f"\","
            f"\""+self.actors+f"\","
            f"\""+self.directors+f"\","
            f"\""+self.sequel+f"\","
            f"\""+self.hitflop+f"\"\n")
        x = myfile.write(mystring)
        if (x):
            return True
        else:
            return False

def main():
    while(1):
        choice = 0
        try:
            choice = int(input(f"Select Choice\n(1) Select Movie By Year\n(2) Select Movie By Genre\n(3) Select Movie By Actor\n(4) Select Movie By Director\n(5) To clear screen\n(6) Add movie to file\n(10) Exit\nEnter Choice::"))
        except ValueError:
            print("Invalid Input")
            continue
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
                os.system('clear')

            case 6:
                add_movie()

            case 10:
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

            if(re.search(f".*{genre}.*",row["genre"],re.IGNORECASE)):  # Here I have used regular expression to find if the specified genre exist in the string
                flag = 1
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

            if(re.search(f".*{actor}.*",row["actors"],re.IGNORECASE)):  # Here I have used regular expression to find if the specified actor exist in the string
                flag = 1
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
            if(re.search(f".*{director}.*",row["directors"],re.IGNORECASE)):  # Here I have used regular expression to find if the specified director exist in the string
                flag = 1
                print(f"{count}. "+row["title"] + f"({row['directors']})")
                count += 1
    if flag == 0:
        print(f"We are sorry there are no movies of director {director} in our dataset")

def add_movie():
    while(1):
        imdb_id = input("Enter IMDB Id (ttXXXXXXX)(Here, X=[0-9]): ")
        if not (re.search("(tt[0-9]{7})",imdb_id)): # Used regular expression for correct ID format
            print("Invalid Id Format")
            continue
        flag = False
        with open("movies.csv","r") as csvfile:
            reader =csv.DictReader(csvfile)
            for row in reader:
                    if(re.search(f".*{imdb_id}.*",row["imdbId"],re.IGNORECASE)):  # Here I have used regular expression to find if the specified director exist in the string
                        flag = True
        if (flag == True):
            print("Record with same ID exist")
            continue
        break
    title = input("Enter Title: ")
    release_year = input("Enter Release Year: ")
    release_date = input("Enter Release Date (DD MMM YYYY)(28 Jan 2024): ")
    genre = input("Enter Genre: ")
    writers = input("Enter Writer: ")
    actors = input("Enter Actors: ")
    directors = input("Enter Director: ")
    sequel = input("Enter Sequel (1 for yes,0 for no): ")
    hitflop = input("Enter Hit-Flop Rating (between 0 to 10 inclusive): ")

    mymovie = Movie(imdb_id,title,release_year,release_date,genre,writers,actors,directors,sequel,hitflop)
    x = mymovie.addmymovie()
    if (x):
        print("The movie is inserted successfully!")
    else:
        print("The movie was not inserted sorry")


if __name__ == "__main__":
    main()