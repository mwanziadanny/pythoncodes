import random
winning_number=random.randint(1,5)
number=int(input('Enter random number:'))
if(number>winning_number):
    print("Too High")
elif(number==winning_number):
    print("You Win")
else:
    print("Too Low")