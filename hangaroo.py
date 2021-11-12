import random

word_list = ['boot', 'library', 'bus', 'cloud', 'airplane', 'computer']
word = list(random.choice(word_list))
attempts = 1*len(word)  # number of attempts
hidden = list('_'*len(word))

print('\n' + 'I am thinking of a word. What word is it?')
while attempts != 0:
    print(''.join(hidden))
    char = input('Guess a letter (' + str(attempts) + ' guesses available): ')
    if char in word:
        index = word.index(char)
        hidden[index] = char
        word[index] = 'X'
    else:
        attempts -= 1
    if len(word)*'X' == ''.join(word):
        print(''.join(hidden))
        print('You win!!')
        exit(0)
print('You loose!!')
