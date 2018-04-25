class Person(object):
    def __inti__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)

    def birthday(self):
        print("Your birthday is today, your now %s today" % self.age)

class Employee(Person):
    def __init__(self, name, age, ability):
        super(Employee, self).__init__()
        self.ability = ability

    def work(self):
        print("You employee, %s, is working hard" % self.name)

    def age(self):
        print("Your employee turn %s today." % self.age)

class Programmer(Employee):
    def __init__(self, name, age, ability):
        super(Programmer, self).__init__(name, age, ability)

    def work(self):
        print("Your programmer, %s, is the best." % self.name)

    def age(self):
        print("Your programmer, %s, just turn %s today" % self.name % self.age)

    def skills(self):
        print("Your programmer, %s, is a fast typer" % self.name)