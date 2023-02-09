#sets
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#finding length of it_companies
print("the length of it_companies:",len(it_companies))
#adding company to it_companies
it_companies.add("twitter")
print(it_companies)
#adding more companies
it_companies.update(["telsa","arewa","spotify"])
print(it_companies)
#removing a company
it_companies.remove("Facebook")
print(it_companies)
#exercise 2
#set 
set_1=A.union(B)
print(set_1)
#set intersection
set_2=A.intersection(B)
print("set intersection is",set_2)
#subset
set_3=A.issubset(B)
print(set_3)
A.isdisjoint(B)
A.union(B) and B.union(A)
A.symmetric_difference(B)
del A
del B
#converting list to set
age_in_set=set(age)
print("the length of age in list",len(age))
print("the length of age in set",len(age_in_set))
#String: An ordered, immutable sequence of characters.
#List: An ordered, mutable sequence of elements of any data type. Lists are defined with square brackets [].
#Tuple: An ordered, immutable sequence of elements of any data type. Tuples are defined with parentheses ().
#Set: An unordered, mutable collection of unique elements of any data type. Sets are defined with curly braces {}.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(len(unique_words))

