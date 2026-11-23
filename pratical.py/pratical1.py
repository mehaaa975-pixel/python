# Write 3 favourite movies into a file

with open("movies.txt", "w") as file:
    file.write("1. Avatar\n")
    file.write("2. Titanic\n")
    file.write("3. Interstellar\n")

# Read the movies from the file

with open("movies.txt", "r") as file:
    movies = file.read()

print("My Favourite Movies:")
print(movies)