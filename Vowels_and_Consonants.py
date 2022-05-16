vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
consonantCount = 0

entry = str(input('Enter a string: '))

for character in entry:
    if character.lower() in vowels:
        vowelCount += 1
    elif character.lower() in consonants:
        consonantCount += 1

print('There is/are', vowelCount, 'vowel(s) and', consonantCount, 'consonant(s) in your string')

