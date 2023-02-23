import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Extract all words using a regular expression
words = re.findall(r'\b\w+\b', paragraph)

# Count the occurrences of each word
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Find the most frequent usr word
most_frequent_word = max(word_counts, key=word_counts.get)

print(most_frequent_word)

import re

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract the numbers using a regular expression
numbers = [int(n) for n in re.findall(r'-?\d+', text)]

# Sort the numbers
sorted_numbers = sorted(numbers)

# Calculate the distance between the two furthest points
distance = sorted_numbers[-1] - sorted_numbers[0]

print(distance)

#exercise 2
import re

def is_valid_variable(first_name):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return bool(pattern.match(first_name))
print(is_valid_variable('first_name') )
print(is_valid_variable('first-name')) 
print(is_valid_variable('1first_name') )
print(is_valid_variable('firstname')) 

#Exercise 3
import re
from collections import Counter

def clean_text(text):
   
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    
    cleaned_text = re.sub(r'\d', '', cleaned_text)
    
    cleaned_text = cleaned_text.lower()
    
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

def most_frequent_words(text):
   
    words = text.split()
    
    word_counts = Counter(words)
    
    top_3 = word_counts.most_common(3)
    return top_3

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))
  
