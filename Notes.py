print("Hello World")

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

