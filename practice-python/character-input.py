"""Program that prints year someone turns 100 years old.

Program that asks the user to enter their name and their age.
Prints out a message addressed to them that tells them the year that they will turn 100 years old based on the
current year provided by the user.

Extra:
- Add on to the previous program by asking the user for another number and printing
out that many copies of the previous message.
- Print out that many copies of the previous message on separate lines.
"""

name = input("What's your name? ")
year = int(input("What's the current year? "))
age = int(input("How old are you? "))
copy_number = int(input("How many times do you want the answer to be printed? "))

result_year = year + (100 - age)

repeated_year_str = copy_number * ("\n" + str(result_year))

print(f"Hello {name}! The year you will turn 100 is: {repeated_year_str}")
