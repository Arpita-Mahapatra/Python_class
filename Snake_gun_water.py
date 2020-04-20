import random

x, y, z = 0, 0, 0 #initializing x,y,z for scores
score = {'you': x, 'computer': y, 'draw': z}
options = ['snake', 'water', 'gun'] 
computer = random.choice(options)
print(computer)
chances=1

while(chances!=0):
    
    you = input("Enter your choice snake,water or gun:")

    if you=='snake' and computer=='gun':

        print('Computer chooses {}'.format(computer)) 
        score['computer'] += 1 #if the condition satisfies computer gets one point
        print("Computer wins!!Better luck next time")
        print(score['computer'])
    elif you == 'gun' and computer == 'snake':
        print('You win! Gun shoots snake!')
        score['you'] += 1 #if the condition satisfies you get one point
        print(score['you'])

    else:
        if you=='snake' and computer=='snake':
             print("Looks Like a tie")
             score['draw'] += 1
             print(score['draw'])

        elif you=='gun' and computer=='gun':
            print("Looks Like a tie")
            score['draw'] += 1 #no. of draw
            print(score['draw'])

        #else:
            #print("Not Valid")



    if you=='gun' and computer=='water':

        print('Computer chooses {}'.format(computer))
        score['computer'] += 1
        print("Computer wins!!Better luck next time")
        print(score['computer'])
    
    elif you == 'water' and computer == 'gun':
        print('You win! water defeats gun!')
        score['you'] += 1
        print(score['you'])

    else:
        if you=='water' and computer=='water':
             print("Looks Like a tie")
             score['draw'] += 1
             print(score['draw'])

        elif you=='gun' and computer=='gun':
            print("Looks Like a tie")
            score['draw'] += 1
            print(score['draw'])

        #else:
            #print("Not Valid")

    if you=='water' and computer=='snake':

        print('Computer chooses {}'.format(computer))
        score['computer'] += 1
        print("Computer wins!!Better luck next time")
        print(score['computer'])
    
    elif you == 'snake' and computer == 'water':
        print('You win! water defeats gun!')
        score['you'] += 1
        print(score['you'])

    else:
        if you=='water' and computer=='water':
             print("Looks Like a tie")
             score['draw'] += 1
             print(score['draw'])

        elif you=='snake' and computer=='snake':
            print("Looks Like a tie")
            score['draw'] += 1
            print(score['draw'])

        #else:
            #print("Not Valid")
    print(chances)
    chances=chances+1
