age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    missing_years = 18 - age
    print("Please wait for" , missing_years," more years to be able to drive.")
    
my_age = 21
your_age = int(input("Enter your age: "))

if your_age > my_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are", age_diff, "year older than me.")
    else:
        print("You are", age_diff, "years older than me.")
elif your_age < my_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am", age_diff, "year older than you.")
    else:
        print("I am", age_diff, "years older than you.")
else:
    print("We are of the same age.")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")
score = int(input("Enter the student's score: "))

if score >= 80 and score <= 100:
    grade = "A"
elif score >= 70 and score <= 89:
    grade = "B"
elif score >= 60 and score <= 69:
    grade = "C"
elif score >= 50 and score <= 59:
    grade = "D"
elif score >= 0 and score <= 49:
    grade = "F"
else:
    grade = "Invalid score. Please enter a score between 0 and 100."

print("The student's grade is:", grade)
month = input("Enter a month: ")

if month == "September" or month == "October" or month == "November":
    season = "Autumn"
elif month == "December" or month == "January" or month == "February":
    season = "Winter"
elif month == "March" or month == "April" or month == "May":
    season = "Spring"
elif month == "June" or month == "July" or month == "August":
    season = "Summer"
else:
    season = "Invalid month"

print("The season is:", season)
fruits = ['banana', 'orange', 'mango', 'lemon']

def add_fruit(fruit, fruits_list):
    if fruit not in fruits_list:
        fruits_list.append(fruit)
        print(fruits_list)
    else:
        print("That fruit already exists in the list")

add_fruit('apple', fruits)

			
	
