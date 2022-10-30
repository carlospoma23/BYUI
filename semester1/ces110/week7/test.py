
secret_word='peruano'
hint="_"*len(secret_word)
print('Welcome to the word guessing game!')
print()
print(f'your hint have {len(secret_word)} letters: {hint}')

play=False

while(play==False):
    
    display=''
    user_word=input('what is your guess? :')
    if(len(secret_word)==len(user_word)):
        i=0
        while i<(len(user_word)):
            j=0
            correct_guess=0
            while j<(len(secret_word)-1):
                if (user_word[i]==secret_word[j]):
                        
                    if j==i:
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
       
    else:
        print('Sorry, the guess myst have the same number of letter as the secret word')
        play=False
    
    print(f'Your hint is: {display}') 
    if(secret_word.lower()==display.lower()):
        print('Congratulations! You guessed it!')
        play=True
    else:
        play=False

       

    
    
    

 