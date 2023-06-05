num = int(input("Insert a number: "))
check = int(input("Insert a number to divide the first number by: "))

if num % 4 == 0:
    print(f"{num} is a multiple of 4.", end='')
elif num % 2 == 0:
    print(f"{num} is an even number.", end='')
else:
    print(f"{num} is an odd number.", end='')

if num % check == 0:
    print(f" {num} can be divided by {check}.")
else:
    print(f" {num} can't be divided by {check}.")
