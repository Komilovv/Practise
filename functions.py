print("======= Define ==== Call")
# Define


def greet(x):
    print("What's up")


def salom(y):
    print("Func is executed")
    return f"Salomun alaykum {y}"

# Call


result1 = greet("Oscar")
print("result1:", result1)

result2 = salom("Otabek")
print(f"result2: {result2}")

print("======= Keyword & default argument ======")
# Define


def give_greet(name, age=21):
    print("arguments are recieved")
    return f"Hi {name}, u r at the age of {age}."


res = give_greet(name="Mikail")
print(res)

print("========= Scope =========")

z = 342  # 3


def calculate(z, f):  # 2
    t = z+f  # 1
    return t


res1 = calculate(89, 98)
print(res1)
