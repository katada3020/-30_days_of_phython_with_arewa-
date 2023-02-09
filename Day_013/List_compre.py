#filtering negative number
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)
#flattening list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist in list_of_lists for sub_sublist in sublist for num in sub_sublist]
print(flattened_list)

result = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
print(result)
# flattening list to another
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened = [[country[0][0].upper(), country[0][0][:3].upper(), city.upper()] for country in countries for city in country[0][1:]]
print(flattened)
#changing list to dictionary
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dictionaries = [{'country': country[0][0].upper(), 'city': city.upper()} for country in countries for city in country[0][1:]]
print(dictionaries)
#concatenated names
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = list(map(lambda x: ' '.join(x[0]), names))
print(result)
#linear slope using lamda
linear_function = lambda x1, y1, x2, y2, type: (y2 - y1) / (x2 - x1) if type == 'slope' else y1 - (x1 * (y2 - y1) / (x2 - x1)) if type == 'y-intercept' else None

x1 = 1
y1 = 2
x2 = 4
y2 = 7
print(linear_function(x1, y1, x2, y2, 'slope'))
print(linear_function(x1, y1, x2, y2, 'y-intercept'))
