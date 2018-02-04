from random import randint

target = randint(0, 100)

print("Welcome to the HI - LO game")

guess = int(input("Guess a number between 1 & 100: "))

while guess != target:
    if target == guess:
        print('That\'s it!  You win!')
    elif guess > target:
        print('Too high')
        guess = int(input("Guess a number between 1 & 100: "))
    else:
        print('Too Low')
        guess = int(input("Guess a number between 1 & 100: "))


print("Correct!")



