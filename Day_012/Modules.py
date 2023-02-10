
#importing random
import random
import string

def random_user_id():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters + string.digits) for i in range(6))

print(random_user_id())
import random
import string

def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))

    letters = string.ascii_lowercase + string.digits

    for i in range(num_ids):
        user_id = ''.join(random.choice(letters) for j in range(num_chars))
        print(user_id)

user_id_gen_by_user()
import random
import string

def rgb_color_gen():
    red = str(random.randint(0, 255))
    green = str(random.randint(0, 255))
    blue = str(random.randint(0, 255))
    return "rgb(" + red + "," + green + "," + blue + ")"

def list_of_hexa_colors(num):
    hexa_colors = []
    hexa_chars = string.hexdigits[0:16]
    for i in range(num):
        color = "#"
        for j in range(6):
            color += random.choice(hexa_chars)
        hexa_colors.append(color)
    return hexa_colors

def list_of_rgb_colors(num):
    rgb_colors = []
    for i in range(num):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors

def generate_colors(color_type, num):
    if color_type == 'hexa':
        return list_of_hexa_colors(num)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return "Invalid color type"

print(rgb_color_gen())
print(list_of_hexa_colors(3))
print(list_of_rgb_colors(3))
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
#exercise 3
import random

def shuffle_list(original_list):
    shuffled_list = original_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list
import random

def random_unique_numbers():
    numbers = random.sample(range(10), 7)
    return numbers
