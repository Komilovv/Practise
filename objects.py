import array
from math import ceil

print(type("Selamun alaykum!"))
print(type(True))
print(type(554))
print(type(array))

print(ceil(5.4))

# ================= Error Handling ================
car = dict(name="Lexus", year=2022)

try:
    a = car.type
    result = car["company"]
    print(f" The result: {result}")
except KeyError as err:
    print("There is no orign state")
except AttributeError as err:
    print(f"No attribute named {err}")
else:
    print("Executed successfully!")
finally:
    print("Finally done!")
