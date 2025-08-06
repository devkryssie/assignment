lucky_number = 7
guess = None
print("welcome to the lucky number game!!!!")
print("guess the lucky number btw 1-10.")
while guess != lucky_number:
    guess = int(input("enter your guess:"))
    if guess < 1 or guess > 10:
        print("pls guess a number btw 1 and 10.")
    elif guess < lucky_number:
        print("too low")
    elif guess > lucky_number:
        print("too high")
    else:
        print("congratulations christy! you guessed the lucky number!")
