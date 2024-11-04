import string

# Main function to handle user input and perform string manipulations
def stringmanupulation(paragraph):
    # Taking input from the user for the paragraph
    paragraph = input("Write a paragraph here\n")
    
    # Loop to continue operations until the user chooses to exit
    while True:
        # Displaying options for the user
        print("Enter 1 to perform word frequency on your paragraph")
        print("Enter 2 to perform character count on your paragraph")
        print("Enter 3 to see the unique words in your paragraph")
        print("Enter 4 to exit")
        
        # Try and except block to handle invalid inputs
        try:
            inputt = int(input("Please enter your choice here: "))
            
            # If the user chooses word frequency
            if inputt == 1:
                wordFrequency(paragraph)
                
            # If the user chooses character count
            elif inputt == 2:
                charCount(paragraph)
                
            # If the user chooses to see unique words
            elif inputt == 3:
                uniqueWords(paragraph)
                
            # If the user chooses to exit
            elif inputt == 4:
                print("\n*******Thank you******\n")
                break  # Break out of the loop to exit
                
            # Handling invalid inputs that are not 1, 2, 3, or 4
            else:
                print("Invalid input, please provide a valid option.")
        
        # Catching exceptions such as non-integer inputs
        except Exception as e:
            print("Please input only integers\n")

# Method to perform word frequency analysis
def wordFrequency(paragraph): 
    print("The word frequency for your paragraph is:")
    
    # Cleaning the text by removing punctuation and converting it to lowercase
    cleaned_text = paragraph.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Splitting the cleaned text into words
    words = cleaned_text.split()
    
    # Using a set to store unique words (though not used for frequency counting)
    res3 = set(words)
    
    # Creating a dictionary with word counts
    res1 = {word: words.count(word) for word in words}
    
    # Printing the word and its frequency
    for word, frequency in res1.items():
        print(f"{word}: {frequency}")

# Method to count the total number of characters (excluding spaces)
def charCount(paragraph):
    # Counting characters excluding spaces
    res2 = len(paragraph.replace(" ", ""))
    
    # Printing the character count result
    print(f"The character count for your paragraph is: {res2}")

# Method to display unique words in the paragraph
def uniqueWords(paragraph):
    # Cleaning the text by removing punctuation and converting it to lowercase
    cleaned_text = paragraph.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Splitting the cleaned text into words
    words = cleaned_text.split()
    
    # Using a set to extract unique words
    res3 = set(words)
    
    # Printing the unique words
    print(f"Here are your unique words:\n{res3}")

# Main method calling the string manipulation function
stringmanupulation('paragraph')

   