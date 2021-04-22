import random

score = 0
lives = 3
words = ['lisa', 'jennine', 'jisooo', 'rose']


def update_clue(guess, secret_word, clue):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            clue[i] = guess

    win = ''.join(clue) == secret_word
    return win


while (len(words) > 0) and (lives > 0):
    random.shuffle(words)
    secret_word = words.pop()
    clue = list('?' * len(secret_word))

    while True:
        print(clue)
        guess = input('ป้อนคำ : ')
        if guess in secret_word:
            win = update_clue(guess, secret_word, clue)

            if win:
                print('ถูกต้อง' + secret_word)
                score = score + 1
                print('score' + str(score))
                break
            else:
                print('ผิด')
                lives = lives - 1
                print('จำนวนชีวิต ' + str(lives))
                if lives == 0:
                    print('เฉลย ' + secret_word)
                    break


print('---------------------------')
print('end game')
print('score ' + str(score))
print('---------------------------')