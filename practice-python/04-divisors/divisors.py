number = int(input("Indicate the number you want to calculate the divisors of: "))

list_divisors = []
for elem in range(1, number + 1):
    if number % elem == 0:
        list_divisors.append(elem)

print(list_divisors)
