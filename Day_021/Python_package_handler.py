 
import re
import requests

# Read the text from the URL
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
text = response.text

# Use regex to remove non-alphanumeric characters and split the text into words
words = re.findall(r'\b\w+\b', text.lower())

# Create an empty dictionary to store the word frequencies
word_freq = {}

# Count the frequency of each word
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Get the 10 most frequent words and their counts
top_10_words = sorted(word_freq.items(), key=get_frequency, reverse=True)[:10]

# Define a helper function to get the frequency of a word from a tuple
def get_frequency(word_tuple):
    return word_tuple[1]

# Print the results
for word, count in top_10_words:
    print(word, count
