range_obj = range(5)
print(range_obj)

for x in "MITchilar":
    print(f"Letter : {x}")

for n in range_obj:
    print("The number is ", n)

person = {"name": "Bobur", "age": 19}
person1 = dict(name="Bobur", age=19)
print(person)
print(person1)

name = person["name"]
age = person.get("age")
nat = person.get("nationality", "Uzbek")
print(f"The person's name is {name}, age is {age}, and nationality is {nat}")

del person1["age"]

for key in person:
    print(f"The key: {key}. Value: {person.get(key)}")
