import random

print("In a very small amount of casaes, the last person picked will pick themself, if this happens just run the program again (this chance is lowered the more participants there are)")
participants = int(input("Number of participants: "))

start = []
finish = []

while participants:
    for i in range(1, participants+1):
        start.append(i)
        finish.append(i)

    for value in start:
        number = random.randrange(0, len(finish))

        while value == finish[number]:
            number = random.randrange(0, len(finish))

        print(f'{value} - {finish[number]}')
        del finish[number]
        
    start.clear()
    finish.clear()
    participants = int(input("Number of participants: "))
