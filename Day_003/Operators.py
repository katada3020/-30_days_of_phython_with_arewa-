age = 21
height = 6.8
#complex 
#calculating the area of a triangle
base= input('Enter base: ')
height = input('Enter height: ')
area = 0.5 * float(base) * float(height)
print('area of a triangle is' ,area
)
#calculating the area of a triangle
a = int(input('Enter a :'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
perimeter =a + b + c
print('perimeter of a rectangle is', perimeter)
#calculating area of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)
#for circle
r = float(input('enter r:'))
pi = 3.14

area = pi *r*r
circumference = 2 * pi * r

print("area of a circle is ",area)
print("circumference is", circumference)
# Calculate the slope y = 2x - 2
a = 2
b = -2
slope = a
x_intercept = -b / a
y_intercept = b

print("Slope:", slope)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

# Calculate the slope and Euclidean distance between the points (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
point_slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("Slope between 2 points:", point_slope)
print("Euclidean Distance:", distance)
# Calculate the slope, x-intercept, and y-intercept of the line y = 2x - 2
a = 2
b = -2
slope = a
x_intercept = -b / a
y_intercept = b

print("Slope:", slope)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)
 
 	#comparison of string
string1 = 'python'
string2 = 'dragon'

len_phython = len(string1)
len_dragon = len(string2)

print("Length of 'python':", phython)
print("Length of 'dragon':", dragon)

if len_string1 != len_string2:
    print("Strings are of different lengths.")

if 'on' in 'python' and 'on' in 'dragon':
    print("'on' is found in both 'python' and 'dragon'")
else:
    print("There is no 'on' in both 'dragon' and 'python'")

sentence = "I hope this course is not full of jargon."
if jargon in sentence:
	print(there is jargon in sentence)
else:
		print("there is no jargon")
		#converting length to string
word = 'python'
length = len(word)
float_length = float(length)
string_length = str(float_length)
print("The length of the word 'python' is:", string_length)
#checking if a number is even
number = 4
if number % 2 == 0:
    print(True)
else:
    print(False)


#modulos
result= 7 // 3
print(result == int(2.7)) 
print(type('10') == type(10)) 
#comparing
result = int('9.8')  
print(result == 10)
hours = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the rate per hour: "))
pay = hours * rate
print("your weekly pay is", + pay)






