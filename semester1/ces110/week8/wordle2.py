
import random


list_words=['mosiah','helaman','moroni','abinadi','samuel','lehi','benjamin']
secret_word=random.choice(list_words)
hint="_"*len(secret_word)
print('Welcome to the word guessing game!')
print()
print(f'your hint have {len(secret_word)} letters: {hint}')

play=False
count=0
while(play==False):
    
    display=''
    user_word=input('what is your guess? :').lower()
    if(len(secret_word)==len(user_word)):
        i=0
        for index in user_word:
            j=0
            correct_guess=0
            for index in user_word:
                if (secret_word[j]==user_word[i] and correct_guess!=1):
                    if i==j:
                        display=display+user_word[i].upper()
                        correct_guess=1
                    else:
                        display=display+user_word[i].lower()
                        correct_guess=1   
                j=j+1   

            if correct_guess==0:
                display=display+'_'   

            i=i+1
            
        play=False
        print(f'Your hint is: {display.lower()}')
        
    else:
        print('Sorry, the guess myst have the same number of letter as the secret word.')
        print()
        play=False
    count=count+1
    if(secret_word.lower()==display.lower()):
        print('Congratulations! You guessed it!')
        print(f'It tool you {count} guesses.')
        play=True
    else:
        play=False

       

    
    
    

 