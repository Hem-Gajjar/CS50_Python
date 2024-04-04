
 # YOUR PROJECT TITLE
    #### Video Demo:  https://youtu.be/wzjwDb-K1xk
    #### Description: "Movie Database Manager" is a Python project designed for efficient management of movie records stored in a CSV file.Users can fetch records based on parameters such as release year, actor, director, and genre, and store new entries seamlessly.With a user-friendly interface and data validation features, it offers a convenient solution for organizing and accessing movie data according to user preferences.

# Project Title: Movie Database Manager

"Movie Database Manager" is a Python project designed for efficient management of movie records stored in a CSV file. Users can fetch records based on parameters such as release year, actor, director, and genre, and store new entries seamlessly. With data validation features, it offers a convenient solution for organizing and accessing movie data according to user preferences.

The "Movie Database Manager" project is a Python application designed to manage a movie database stored in a CSV file. It allows users to fetch and store movie records based on various parameters such as release year, actor, director, and genre. To ensure the correctness and reliability of the implemented methods in project.py, a separate testing file named test_project.py has been created. This file contains unit tests to verify the functionality of each method defined in project.py. By running these tests, developers can ensure that the application behaves as expected and that any modifications made to the code do not introduce unintended side effects or bugs.

## Execute Project

To execute this project run

```bash
  python project.py
```


## Documentation
**Movie Database Manager Documentation**

**Introduction:**
The "Movie Database Manager" is a Python-based application designed to facilitate the management of a movie database stored in a CSV file. This comprehensive documentation provides an in-depth explanation of the project structure, implementation details, methods, testing procedures, and usage instructions.

**Project Structure:**
The project comprises two primary files:
1. **project.py:** This file contains the core logic and implementation of the application, including class definitions and methods for managing movie records.
2. **test_project.py:** This file contains unit tests to verify the functionality of methods defined in `project.py`, ensuring the reliability and correctness of the application.

**Implementation Details:**

**1. Movie Class:**
The `Movie` class represents a movie entity and encapsulates various attributes such as IMDb ID, title, release year, release date, genre, writers, actors, directors, sequel status, and hit-flop rating. Below are the attributes of the `Movie` class:

- **imdb_id:** IMDb ID of the movie.
- **title:** Title of the movie.
- **release_year:** Year of movie release.
- **release_date:** Date of movie release.
- **genre:** Genre(s) of the movie.
- **writers:** Writers of the movie.
- **actors:** Actors in the movie.
- **directors:** Director(s) of the movie.
- **sequel:** Sequel status of the movie (1 for yes, 0 for no).
- **hitflop:** Hit-flop rating of the movie (scale of 0 to 10).

Additionally, the `Movie` class includes an `addmymovie()` method to add a new movie record to the database file (`movies.csv`). This method constructs a formatted string containing movie details and appends it to the CSV file.

**2. Main Functionality:**
The `main()` function serves as the entry point of the application. It presents users with a menu-driven interface to interact with the movie database. The menu options include:
- Select Movie By Year
- Select Movie By Genre
- Select Movie By Actor
- Select Movie By Director
- Clear Screen
- Add Movie To File
- Exit

Users can input their choice, and the corresponding functionality will be executed accordingly.

**3. Fetching Movie Records:**
The application provides methods to fetch movie records based on different criteria such as year, genre, actor, and director. The following methods are responsible for fetching records:

- **select_by_year(year):** Fetches movies released in the specified year from the database file. It iterates through the CSV file and prints the titles of movies released in the given year.
- **select_by_genre(genre):** Fetches movies of the specified genre from the database file. It utilizes regular expressions to match genre patterns and prints the titles along with their genres.
- **select_by_actor(actor):** Fetches movies featuring the specified actor from the database file. It performs case-insensitive pattern matching using regular expressions and prints the titles along with the actors.
- **select_by_director(director):** Fetches movies directed by the specified director from the database file. It uses regular expressions to match director patterns and prints the titles along with the directors.

These methods ensure efficient retrieval of movie records based on user-specified criteria.

**4. Adding Movie Records:**
The `add_movie()` function guides users through the process of adding a new movie record to the database. It prompts users to input various details such as IMDb ID, title, release year, release date, genre, writers, actors, directors, sequel status, and hit-flop rating. Input validation is performed to ensure correctness, and the new movie record is appended to the CSV file using the `addmymovie()` method of the `Movie` class.

**Testing:**
The `test_project.py` file contains a suite of unit tests to validate the functionality of methods defined in `project.py`. Each test case covers different scenarios to ensure the reliability and correctness of the application.

**Usage:**
To utilize the "Movie Database Manager" application, users can execute `project.py` in their Python environment. They will be presented with a menu-driven interface where they can select various options to interact with the movie database, including fetching movies, adding new movies, and exiting the application.

**Conclusion:**
The "Movie Database Manager" project offers a robust and user-friendly solution for managing movie databases. Through detailed documentation, users can gain a comprehensive understanding of the project structure, implementation details, methods, testing procedures, and usage instructions. This documentation serves as a valuable resource for users, developers, and stakeholders involved in utilizing or contributing to the project.
