import random
choose=("stone","paper","scissor")
computer=random.choice(choose)
print(choose)
user=input("Enter any element for above : ")
user=user.lower()
if user==computer:
    print("Match tie")
elif (user == "stone" and computer=="paper" or 
        user== "paper" and computer == "scissor" or 
        user=="scissor" and computer == "stone" ):
    print("You loose")
else:
    print("You won")