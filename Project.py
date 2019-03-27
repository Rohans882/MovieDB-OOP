from find_method import find_by_attribute

class Moviedb:

    def __init__(self):
        self.movies = []

    def __len__(self):
        return len(self.movies)

    def __str__(self):
        return f"This is a movie database containing {len(self)} movies!\n"

    def __repr__(self):
        return f"Movies: {self.movies}"

    def __getitem__(self, item):
        return self.movies[item]

    def add_movie(self):
        name = input("Enter the movie name: ")
        director = input("Enter the movie director: ")
        year = input("Enter the movie release year: ")

        self.movies.append({
            'name': name,
            'director': director,
            'year': year
        })

    def show_movies(self, movies_list):
        for movie in movies_list:
            self.show_movies_details(movie)

    def show_movie_details(self, movie):
        print(f"Name: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['year']}")

    def find_movie(self):
        find_by = input("Property looking for: ")
        looking_for = input("What are you looking for? ")
        found_movies = find_by_attribute(self.movies, looking_for, lambda x: x[find_by])
        if found_movies:
            self.show_movies(found_movies)
        else:
            print("No movies Found")

    def find_by_attribute(items, expected, finder):
        found = []
        for i in items:
            if finder(i) == expected:
                found.append(i)
        return found

def menu():
    user_input = input("'add' to add a movie:\n'list' to see your movies\n'find' to find a movie\n'quit' to quit: ")
    new_movie = Moviedb()
    while user_input != 'quit':
        if user_input == 'add':
            new_movie.add_movie()
            print(new_movie[0])
        elif user_input == 'list':
            print(new_movie)
        elif user_input == 'find':
            new_movie.find_movie()
        else:
            print("Can't find proper command. ")
        user_input = input("\nEnter 'add' to add a movie.\nEnter 'list' to see your movies.\nEnter 'find' to find a movie.\nEnter 'quit' to quit: ")

menu()




