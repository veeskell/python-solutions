def is_palindrome(word):

    lower_word = word.lower()

    for n in range(len(word) // 2):
        if not lower_word[n] == lower_word[-n - 1]:
            return False
    return True

word = input("Type a word to check if it is a palindrome: ")

if is_palindrome(word):
    print("The word is a palindrome.")
else:
    print("The word isn't a palindrome.")
