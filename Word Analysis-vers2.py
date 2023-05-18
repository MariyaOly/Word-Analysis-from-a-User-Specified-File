import os
import re
from collections import Counter

def get_most_common_long_words(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        text = file.read()

    # Split the text into individual words using regular expressions
    words = re.findall(r'\b\w+\b', text)

    # Filter words by length (more than three characters) and count their frequency
    filtered_words = [word.lower() for word in words if len(word) > 3]
    word_counts = Counter(filtered_words)

    # Find the most common word
    most_common_word = word_counts.most_common(1)[0][0]

    # Find the longest English word
    english_words = [word for word in words if word.isalpha()]
    longest_word = max(english_words, key=len)

    return most_common_word, longest_word

# Prompt the user for a file name
filename = input("Enter the file name: ")

# Check if the specified file exists
if not os.path.isfile(filename):
    print("File does not exist.")
else:
    # Call the function to get the results
    most_common, longest = get_most_common_long_words(filename)

    # Display the results
    print("Most frequently occurring word (more than three characters):", most_common)
    print("Longest word in English:", longest)
