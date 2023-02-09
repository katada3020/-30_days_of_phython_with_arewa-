#create empty dictionary
dog = {}
#adding items to the dictionary
dog["name"] = "blade"
dog["colour"] = "black"
dog["breed"] =  "chichi"
dog["legs"] = "4"
dog["age"] = "7"
print(dog)
#creating a student dictionary
student_dict = {}
student_dict["first_name"] = "nasiru"
student_dict["last_name"] =   "mohammed"
student_dict["gender"] = "male"
student_dict["age"] = "21"
student_dict["marital status"] = "single"
student_dict["skills"] = ["python","analytics"]
student_dict["city"] = "kaduna"
student_dict["address"] = '''no 1 yoruba close hayinbanki kaduna ''' 
print(student_dict)
print("the length of student is",len(student_dict))
skills = student_dict['skills']
skills_data_type = type(skills)
print("data type is",skills_data_type)
 #Modify the skill
student_dict["skills"] += ["CSS", "HTML"]
print("Modified Skills:", student_dict["skills"])

# Get the dictionary keys as a list
keys = list(student_dict.keys())
print("Dictionary keys:", keys)

# Get the dictionary values as a list
values = list(student_dict.values())
print("Dictionary values:", values)

# Change the dictionary to a list of tuples using items()
student_items = list(student_dict.items())
print("Student items as list of tuples:", student_items)

# Delete one of the items in the dictionary
del student_dict["city"]
print("Dictionary after deleting city:", student_dict)

# Delete one of the dictionaries
del student_dict
