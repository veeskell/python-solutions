name = input("What's your name? ")
year = int(input("What's the current year? "))
age = int(input("How old are you? "))
copy_number = int(input("How many times do you want the answer to be printed? "))

result_year = year + (100 - age)

repeated_year_str = copy_number * ("\n" + str(result_year))

print(f"Hello {name}! The year you will turn 100 is: {repeated_year_str}")
