vowels = ('a', 'e', 'i', 'o', 'u')
text = input()

for letter in text:
    if letter in vowels:
        print('vowel')
    elif letter.isalpha():
        print('consonant')
    else:
        break
