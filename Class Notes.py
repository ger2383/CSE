# # Defining a class
# class Cheeseburger(object):
#     def __init__(self, patty_type, cheese):  # Two underscores before and after
#         self.patty = patty_type
#         self.cheese = cheese
#         self.eaten = False
#
#     def give(self, name):
#         print(name + "is thankful")
#
#     def cut(self):
#         print("You cut the cheeseburger")
#
#     def eat(self):
#         print("You eat the cheesburger")
#         self.eaten = True
#
#
# # Instanting (The creation of) two cheeseburgers
# burger1 = Cheeseburger("Beef", "Havarti")
# burger2 = Cheeseburger("Bacon", "Swiss")
#
# print(burger1.eaten)
# print(burger2.cheese)
#
# burger1.eat()
# print(burger1.eaten)
# print(burger2.eaten)


class car(object):
    def __init__(self, name, color, num_of_doors, hp):
        self.colors = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passengers = 0
        self.name = name
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print("Nothing Happens")
        else:
            self.running = True
        print("The car starts.")

    def move_forward(self):
        if self.running:
            print("You move forward")
        else:
            print("Nothing Happans")

    def turn_off(self):
        if self.running:
            self.running = False
            print("You turn the car off")
        else:
            print("The car is already off")

    def go_for_drive(self, passengers):
        print("%d passengers get in." % passengers)
        self.passengers = passengers
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out." % passengers)
        self.passengers = 0


my_car = car("GTR R35", "Blue", 1, 8000)


class Vehicle(object):
    def __init__(self, source, material, seat, speed, passengers):
        self.power_source = source
        self.material = material
        self.seat_location = seat
        self.max_speed = speed
        self.passengers = passengers
    def move(self):
        print("You move forward")

    def change_direction(self):
        print("You change directions")



class Car(Vehicle):
    def __init__(self,  material, seat, speed, passengers, windows):
        super(Car, self).__init__('engine', material, seat, speed, passengers)
        self.windows = windows

    def roll_down_windows(self):
        print("You roll thw windows down")

    def turn_on(self):
        print("You turn on the key and the engine starts")

test_car = Car('Aluminum', 'Driver side', 140, 2, True)
test_car.change_direction()



class KeylessCar(Car):
    def __init__(self,  material, seat, speed, passengers, windows):
        super(KeylessCar, self).__init__(material, seat, speed, passengers, windows)

    def turn_on(self):
        print("You push the button and the car turns on")


test_car.turn_on()
cool_car = KeylessCar('Aluminum', 'Driver side', 140, 2, True)
cool_car.turn_on()


class Tesla(KeylessCar):
    def __init__(self, material, seat, speed, passengers, windows):
        super(Tesla, self).__init__( material, seat, speed, passengers, windows)

    def fly(self):
        print("You launch the car into low earth orbit")

    def turn_on(self):
        Car.turn_on(self)
