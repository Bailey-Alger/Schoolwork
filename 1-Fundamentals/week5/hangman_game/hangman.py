import hangman_strings
import hangman_words

hiddenWord = hangman_words.word()
hiddenWordList = list(hiddenWord)
wrong = 0
displayWordList = []
for char in hiddenWord:
    displayWordList.append('_')


def display():
    hangman_strings.display(wrong)
    print(' '.join(displayWordList))
    print()


print(' HANGMAN ')
while '_' in displayWordList:
    if wrong == 6:
        display()
        print('You lose!')
        quit()
    display()
    guess = input()
    if guess == '_':
        continue
    if guess not in hiddenWordList:
        wrong += 1
        continue
    while guess in hiddenWordList:
        displayWordList[hiddenWordList.index(guess)] = guess
        hiddenWordList[hiddenWordList.index(guess)] = '_'
display()
print('Congradulations!')
