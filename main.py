import random

score = 0
lives = 3
words = ['lisa', 'jennine', 'jisoo', 'rose']


def update_clue(guess, secret_word, clue):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            clue[i] = guess
    result = ''.join(clue) == secret_word
    return result


def hint_clue(clue, secret_word):
    rnd_word = random.randint(0, len(secret_word)-1)
    list_word = list(secret_word)
    for i in range(len(secret_word)):
        if list_word[i] == secret_word[rnd_word]:
            clue[i] = secret_word[rnd_word]
    return clue



while (len(words) > 0) and (lives > 0):
    random.shuffle(words)
    secret_word = words.pop()
    clue = list('?' * len(secret_word))

    while True:
        print(hint_clue(clue, secret_word))
        guess = input('ป้อนคำ : ')
        if guess in secret_word:
            win = update_clue(guess, secret_word, clue)

            if win:
                print('ถูกต้อง' + secret_word)
                score = score + 1
                print('score' + str(score))
                break

        else:
            print('ผิด' + str(lives))
            lives = lives - 1
            if lives == 0:
                print('เฉลย ' + secret_word)
                break


