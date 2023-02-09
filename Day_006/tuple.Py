empty_tuple=()
brothers = ('ahmad','abdul','yusuf','tanimu')
sisters = ('amira','yusra','asmau')
print('my brothers:',brothers)
print('my sisters:',sisters)
siblings = brothers + sisters
print(siblings)
my_siblings= list(siblings)
num_siblings = len(my_siblings)
print('my siblings no:',siblings)
parent = ('daddy','mummy')
family_members = siblings + parent
print(family_members)
#unpacking parent
siblings, parents = family_members[:num_siblings], family_members[num_siblings:]
print("Siblings:", siblings)
print("Parents:", parents)
# Create fruits, vegetables and animal products tuples
fruits = ('apple', 'banana', 'orange')
vegetables = ('potato', 'carrot', 'cucumber')
animal_products = ('milk', 'cheese', 'eggs','fish')

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle = len(food_stuff_tp) // 2
print(middle)
# Create fruits, vegetables and animal products tuples
fruits = ('apple', 'banana', 'cherry')
vegetables = ('potato', 'carrot', 'cucumber')
animal_products = ('milk', 'cheese', 'eggs')

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle = len(food_stuff_tp) // 2
middle_items_tp = food_stuff_tp[middle-1:middle+2]
middle_items_lt = food_stuff_lt[middle-1:middle+2]

print("Middle items from tuple:", middle_items_tp)
print("Middle items from list:", middle_items_lt)

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print("Is Estonia a nordic country:", 'Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print("Is Iceland a nordic country:", 'Iceland' in nordic_countries)
