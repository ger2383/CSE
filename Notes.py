'''print("Hello World")

 # Ger Yang

a = 4
b = 3

print(3 + 5)
print(5 - 3)
print(3 * 5)
print(6 / 2)
print(3 ** 2)

print()
print("Try to figure out how this works")
print(13 % 12)

# the "%" sign is a modules. It finds the reminder.

car_name = "Wiebe Mobile"
car_type = "BMW"
car_cylinders = 8
car_mpg = 5000.9

print("I have a car called %s. It's pretty nice." % car_name)
print("I have a car called %s. It's a %s." % (car_name, car_type)) # watch the order

# Here is where we get a little fancy
print("What is your name?")
name = input(">_ ")
print("Hello %s." % name)

age = input("How old are you?")
print("%s?! Thats really old. You belong in a retirement home." % age)
# Functions


def print_hw():
    print("Hello World.")
    print("Enjoy the day.")


print_hw()


def say_hi(name): # Name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("John")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age += 1  # age = age + 1
    print("next year, %s will be %d years old"% (name, age))


print_age("Ger", 14)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7 * x -4


print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "F"


grade_calc(92)


def happy_bday (name):
    print("Happy Birthday to you" +',')
    print("Happy Birthday to you" + ',')
    print("Happy Birthday dear " + name + ',')
    print("Happy Birthday to you" + '.')
happy_bday("Ger")


# Loops

for num in range (10):
    print(num + 1)

a = 1
while a < 10:
    print(a)
    a += 1

# Random Numbers
import random # This should be on the line 1
print(random.randint(0, 1000)



# Recasting
c = '1'
print(c == 1),   # we have a string and an int
print(c == str(1)),


# comparisons

print(1 == 1), # use a double equal sign
print(1 !=2), # 1 is not equal to 2
print(not False)

# random.randint(1,50)
# print(winning_number)
# player_guess = int(input("Choose a number between 1 and 50"))
# def player_guess(winning_number):
#     if player_guess == winning_number:
#         print("you win!")



# while guesses < 5:
#     guess = input(" ")
#     guess = int(guess)
#
# guesses = guesses + 1
#
# if guess > number:
#     print("You guess to low guess higher")


#Lists
'''
# the_count = [1, 2, 3, 4, 5]
# cheeseburger_ingredients = ['cheese', "beef", "sauce", "sesame seed bun", "avacodo", "onions"]
# print(cheeseburger_ingredients[0])
# print(cheeseburger_ingredients[3])
# (len(cheeseburger_ingredients))
#
# # Going through lists
# for generic_item_name in the_count:
#     print(generic_item_name)
#
# for num in the_count:
#     print(num * 2)
#
# length = len(cheeseburger_ingredients)
# range(5)  # A list of the numbers 0 through 4
# range(len(cheeseburger_ingredients))  # Generate a list of all indices
#
# for num in range(len(cheeseburger_ingredients)):
#     item = cheeseburger_ingredients[num]
#     print("The item at index %d is %s" % (num, item))
#
# # Recasting into a list
# str0ne = "Hello World!"
# list0ne = list(str0ne)
# print(list0ne)
# list0ne[11] = '.'
# print(list0ne)
#
# # Adding things to a list
# cheeseburger_ingredients.append("Fries")
# print(cheeseburger_ingredients)
#
# # Remove things from a list
# cheeseburger_ingredients.pop(1)
# print(cheeseburger_ingredients)
# cheeseburger_ingredients.remove("cheese")
# print(cheeseburger_ingredients)
#
# # Getting the alphabet
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
#
# # Making things Lowercase
# strTwo = "ThIs Is A VeRy Odd SenTeNCe"
# lowercase = strTwo.lower()
# print(lowercase)

# Dictionaries - made up of key: value pair

dictionary = {'name': 'Lance', 'age': 26, 'height': 6 * 12 + 2}

# Accessing things from dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Add a pair to a dictionary
dictionary["profession"] = "telemarketer"


large_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print(large_dictionary['NY'])

larger_dictionary = {
    'CA': [
        'Fresno',
        "San Francisco",
        "San Jose"
    ],
    'AZ': [
        "Phoenix",
        "Tuscon"
    ],
    'NY': [
        "New York City",
        "Brooklyn",
    ]
}
print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])
print(larger_dictionary['AZ'][0])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Navada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    },
}
current_node = largest_dictionary['CA']
print(current_node["BORDER ST"][1])
current_node = largest_dictionary['NY']
print(current_node['NAME'])
print(current_node['POPULATION'])

