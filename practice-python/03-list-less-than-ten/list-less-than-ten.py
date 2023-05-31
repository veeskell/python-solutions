exercise_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Say a number: "))

l = []
for element in exercise_list:
    if element < number:
        l.append(element)

print(l)

"""
# Can also be written in one line using list comprehension:

exercise_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([i for i in exercise_list if i < number])

# Can also be done through a filter function:

def is_less_than_five(x):
  return x < 5

print(list(filter(is_less_than_five, exercise_list)))

# Or simplified through the usage of a lambda function:

print(filter(lambda x: x < 5, exercise_list))

"""
