vowels = ['a','e','i','o','u']
words = input("enter a word to check  ")
found = []
for letter in words:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found :           
        print(vowels)