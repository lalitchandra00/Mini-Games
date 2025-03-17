import random
number=random.randint(1,10)
for chance in range(0,3):
    guess_no=int(input("Enter the no. from 1 to 10:" ))
    if guess_no==number:
        print("You won")
        break
    elif guess_no<number:
        print("Choose Higher no.")
    elif guess_no>number:
        print("Choose lower no.")