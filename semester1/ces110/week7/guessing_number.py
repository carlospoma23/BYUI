import random

print('What is the magic number?')
ans='yes'

while ans=='yes':
    
    numberale=random.randint(1,20)
    guest=-1
    count=0
    while guest!=numberale:
        guest=int(input('What is your guest: '))        
        count=count+1    
        if guest<numberale:
            print('Higher')
        elif guest>numberale:
            print('Lower')
        else:
            print(f'You guessed it!')

    print(f'It took you {count} guesses')

    ans=input('Would you like to play again (yes/no)? ')

print('Thank you for playing. Good bye.')