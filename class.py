"""We learn Classes"""


# class Person():
#     # state
#     mes = "This is a class named Person"

#     # constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # methods

#     def introduce(self):
#         print(f"Hello User, I am {self.name}.")

#     def get_age(self):
#         print(f"I am {self.age} years old.")


# person1 = Person("Steve", 67)
# person2 = Person("Ahmad", 30)
# # state
# print(person1.name)
# print(person2.age)
# # method
# person1.introduce()
# print(person2.get_age())

# new_mes = Person.mes
# print(new_mes)

# The special methods of Python

class Car():
    desc = "The class makes car objects"

    def __new__(cls, *args):
        print("__new__")
        return super(Car, cls).__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # methods
    def start_engine(self):
        print(f"{self.name} started the engine")

    def stop_engine(self):
        print(f"{self.name} stoped the engine")

    def __str__(self):
        return f"{self.name} was produced in {self.year}"

    def __call__(self):
        print("Object is called as a function")


my_car = Car("Mercedes-AMG", 2026)
my_car.start_engine()
my_car.stop_engine()

y_car = Car("Genisus", 2020)
print(y_car)
y_car()
