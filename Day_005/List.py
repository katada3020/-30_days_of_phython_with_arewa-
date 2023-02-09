
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


print(it_companies)

# Printing the number of companies in the list
print(len(it_companies))

# Printing the first, middle and last company
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

# Printing the list 
it_companies[0] = 'Alphabet (Google)'
print(it_companies)

# Adding an IT company to it_companies
it_companies.append('Tesla')
print(it_companies)

# Inserting an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Netflix')
print(it_companies)



# Joining the it_companies with a string '#;  '
print("#; ".join(it_companies))

# Checking if a certain company exists in the it_companies list
print('Microsoft' in it_companies)

# Sorting the list using sort() method
it_companies.sort()
print(it_companies)

# Reversing the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slicing out the first 3 companies from the list
print(it_companies[:3])

# Slicing out the last 3 companies from the list
print(it_companies[-3:])

# Slicing out the middle IT company or companies from the list
middle = len(it_companies)//2
print(it_companies[middle-1:middle+2])

# Removing the first IT company from the list
del it_companies[0]
print(it_companies)

# Removing the middle IT company or companies from the list
del it_companies[middle-1:middle+2]
print(it_companies)

# Removing the last IT company from the list
it_companies.pop()
print(it_companies)

# Removing all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroying the IT companies list
del it_companies
# Joining the lists
full_stack = front_end + back_end
print(full_stack)

# Inserting
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()

# Find the min and max age
min_age = min(ages)
max_age = max(ages)

# Add the min and max age to the list
ages.append(min_age)
ages.append(max_age)

# Find the median age
if len(ages) % 2 == 0:
    median = (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
else:
    median = ages[len(ages)//2]

# Find the average age
average = sum(ages) / len(ages)

# Find the range of the ages
range_ages = max_age - min_age

# Compare the value of (min - average) and (max - average)
diff_min = abs(min_age - average)
diff_max = abs(max_age - average)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Find the middle country(ies) in the list
if len(countries) % 2 == 0:
    middle = countries[len(countries)//2 - 1: len(countries)//2 + 1]
else:
    middle = countries[len(countries)//2]

# Divide the countries list into two equal lists
first_half = countries[:len(countries)//2 + 1]
second_half = countries[len(countries)//2 + 1:]

# Unpack the first three countries and the rest as scandic countries
(china, russia, usa, *scandic) = countries


