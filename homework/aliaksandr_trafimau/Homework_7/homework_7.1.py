a = 12

while True:
    user_input = int(input("Guess the number: "))
    if user_input == a:
        print("Congratulations! You guessed it!")
        break
    else:
        print("Try again")
