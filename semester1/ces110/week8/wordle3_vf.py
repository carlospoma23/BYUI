
import random

list_words=['nephi','jacob','enos','mosiah','jarom','omni','helaman','moroni','abinadi','samuel','lehi','benjamin']

answer=False
while answer==False:
    secret_word=random.choice(list_words)
    hint="_"*len(secret_word)
    play=False
    count=0
    print('**** Welcome to the word guessing game! ****')
    print('learn by playing')
    print('In this game you will have to discover the name of a prophet from the book of mormon')
    print("READY, LET'S GO")
    print("*************************************************************************************")
    print()
    print(f'your hint have {len(secret_word)} letters: {hint}')
    print()
    while(play==False):
        
        display=''
        user_word=input('what is your guess? :').lower()
        if(len(secret_word)==len(user_word)):
            i=0
            for index in user_word:
                j=0
                correct_guess=0
                for index in user_word:
                    if (secret_word[j]==user_word[i] and correct_guess != 1):
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
            if (secret_word.lower()!=display.lower()):
                print(f'Your hint is: {display.lower()}')
        else:
            print('Sorry, the guess must have the same number of letter as the secret word.')
            print()
            play=False
        count=count+1
        if(secret_word.lower()==display.lower()):
            print('Congratulations! You guessed it!')
            print(f'It took you {count} guesses.')
            play=True
    
    correct=False
    while correct==False:
        answer=input('Do you want to play again (yes/no) :')
        if (answer=='yes'):
            answer=False
            correct=True
        elif(answer=='no'):
            print('Thank you for your time')
            answer=True
            correct=True
        else:
            print("Please respond yes or no")
            correct=False
    
                
       
    
            


       

    
    
    

 