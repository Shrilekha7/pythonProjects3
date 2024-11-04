# 5. **Movie Recommendation System (Final Project)**  

# Initialize genres and movie list
genres = set()  # This will store unique genres

# List of movie dictionaries, each containing a title and genre
movies = [
    {"title": 'Persuit of Happyness', "genre": 'Sentimental'},
    {"title": 'Avengers', "genre": 'Scientific'},
    {"title": 'Interstellar', "genre": 'Scientific'},
    {"title": 'Predestination', "genre": 'Sentimental'},
    {"title": 'Chandamama', "genre": 'Family'},
    {"title": 'Tulasi', "genre": 'Romance'},
    {"title": 'Love Story', "genre": 'Romance'},
    {"title": 'Devara', "genre": 'Action'},
    {"title": 'Hit', "genre": 'Crime'}
]

# Populate the 'genres' set with unique genres from the 'movies' list
for item in movies:
    genres.add(item["genre"])

# Function to recommend movies based on the user's selected genre
def movieRecommendation():
    print("*WELCOME to Movie Recommendation System*")
    
    # Display the list of available genres
    print("These are the genres you have : ", genres)
    genre1=input("Enter your preferred genre : ").capitalize()
    
    # Initialize a flag to check if any movies are found for the selected genre
    found = False
    
    # Loop through the movies to find matches for the selected genre
    for movie in movies:
        if movie['genre'] == genre1:  
            print("Here are your movie recommendations :", movie['title'])
            found = True
    
    # Inform the user if no movies are found for the selected genre
    if not found:
        print("Sorry, no movies found for that genre. Please try again.")

# Main program loop to keep asking for user input until they choose to exit
while True:
    print("Please enter 1 for Movie Recommendation and 0 to Exit")
    
    # Get user input to either recommend movies or exit
    choice = int(input("Enter a number: "))
    
    # If the user selects 1, call the movie recommendation function
    if choice == 1:
        movieRecommendation()
    
    # If the user selects 0, break the loop and exit the program
    elif choice == 0:
        break
    
    # Handle invalid inputs that are not 1 or 0
    else:
        print("Please enter a valid number (1 for recommendation, 0 to exit)")
      




