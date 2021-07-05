import random
s=[]
guess=random.randrange(1,50)
user=int(input("Enter number: "))
s.append(user)
while user!=guess:
    if guess < user:
        print("Try lower")
        user = int(input("Enter number: "))
        s.append(user)
    else:
        print("Try higher")
        user = int(input("Enter number: "))
        s.append(user)
print("You nailed it !!")
print("Number of attempts: ",len(s))
class fina():

    if len(s)<10:
        print("Congrats you won 5 stars","*"*5)
    elif 10<=len(s) and len(s)<=15:
        print('Congrats you won 3 stars','*'*3)
    elif len(s)>=20:
        print("Better luck next time",'*')
    else:
        print('You won 2 stars only','**')
fina()
