print()
print()
print()


print(                    ''' Hand Cricket'''      )
print()
print()

print()
print()

import random

print("1. Bat")
print("2. Bowl")
user = int(input("Enter 1/2 : "))
if user == 1:
    us = 0
    print("You are batting")
    print()
    while str:
        bat = int(input("[0,1,2,3,4,5,6]  : "))
        print()
        if bat in [0,1,2,3,4,5,6]:
            computer= random.randint(0,2)
            if bat != computer:
                print("computer =", computer)
                us = us + bat
                print("Your runs = ", us)
                print()
                continue
            else :
                print("You are out")
                print("Computer =", computer)
                print("Total runs ", us)
                print()
                break
        else:
            print("Please choose valid number :")        


cs=0   
print("Now you are bowling : ") 

while str:
    bowl = int(input("[0,1,2,3,4,5,6] : "))
    print()
    if bowl in [1,2,3,4,5,6]:
        computer= random.randint(0,3)
        if bowl != computer:
            print("computer =", computer)
            print ("bowl =",bowl)
            print()
            cs = cs + computer 
            print("Computer's run : ", cs)
            print()
            continue
        else :
            print("Compueter is out")
            print("computer = ", computer) 
            print("Total runs ", cs)
            print()
            break
if cs>us:
                print("Computer won, You lose")
                print()
else:
                print("You Won")
                print()
        
    
        