# print("========== number ============")
# count = 100
# c_type = type(count)
# print(f"The count is {count} and the type is {c_type}")

# x = count.bit_count()
# y = count.numerator
# print(x, y)

# print("========== string ============")

# course = "AI Agentic FullStack"
# z = type(course)
# print(f"the type of the course > {z}")
# z = course.title()
# print(z)
# a = course.upper()
# print(a)
# b = course.replace("AI", "AGI")
# print(b)

print("========== boolean ============")

y1 = input("Enter number >")
resultt = y1.isnumeric()
print(f"The input value is {resultt}")

test_falsy = "" or False or None or 0
print("The test is ", bool(test_falsy))

test_truthy = "HUUU"
print("The test is ", bool(test_truthy))
