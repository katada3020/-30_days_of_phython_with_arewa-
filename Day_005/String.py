# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
thirty_days_of_python = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print(thirty_days_of_python)

# Concatenate the string
coding_for_all = 'Coding ' + 'For ' + 'All'
print(coding_for_all)

# Declare a variable named company and assign it to an initial value "Coding For All"
company = "Coding For All"

print(company)

# Print the length of the company string using len() method and print()
print(len(company))

# Change all the characters to uppercase letters using upper() method
print(company.upper())

# Change all the characters to lowercase letters using lower() method
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())


print(company[7:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods
print("Coding" in company)
string = "Coding For All"
string = string.replace("Coding", "Python")
print(string)
string = "Python for Everyone"
string = string.replace("Everyone", "All")
print(string)
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = string.split(", ")
print(companies)
string = "Coding For All"
print(string[0])
string = "Coding For All"
last_index = len(string) - 1
print(last_index)
string = "Python For Everyone"
joining= "".join([word[0] for word in string.split(" ")])
print(joining)
string = "Coding For All"
index = string.index("C")
print(index)
string = "Coding For All"
print(string.index("F"))
string = "Coding For All People"
print(string.rfind("l"))
string = "You cannot end a sentence with because because because is a conjunction"
print(string.find("because"))
string = "You cannot end a sentence with because because because is a conjunction"
print(string.rindex("because"))
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
#using formatting method
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

print("{} + {} = {}".format(8, 6, 8 + 6))
print("{} - {} = {}".format(8, 6, 8 - 6))
print("{} * {} = {}".format(8, 6, 8 * 6))
print("{} / {} = {:.2f}".format(8, 6, 8 / 6))
print("{} % {} = {}".format(8, 6, 8 % 6))
print("{} // {} = {}".format(8, 6, 8 // 6))
print("{} ** {} = {}".format(8, 6, 8 ** 6))



