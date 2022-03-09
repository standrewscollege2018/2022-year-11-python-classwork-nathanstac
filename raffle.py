''' Raffle program '''

# Set up list to store names of entrants
names = []
import random
keep_asking = True
print("welcome to the raffle program")
print("what is the prize being raffled")
prize = input()
print(f"what is the value of {prize} ")
value = input()

while keep_asking == True:
    print("enter the name of entrant")
    name = input()
    if name.lower() == "end":
        keep_asking = False
    else:
        names.append(name)
print(names)
print("these are the people who have entered for the rafffle")
winner = random.randint(0,len(names)-1)
print(f"Winner of the {prize} valued at ${value} is.... {names[winner]}")
