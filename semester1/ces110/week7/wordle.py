secret_word='peruano'
hint="_"*len(secret_word)
user_word=''
print('Welcome to the word guessing game!')
print()
display=''
print(f'your hint have {len(secret_word)} letters: {hint}')

i=0
user_word=input('what is your guess? ').lower()
if len(user_word)!=len(secret_word):
    print('Sorry, the guess myst have the same number of letter as the secret word')
else:   
    while i<(len(secret_word)):
        j=0
        correct_guest=0
        while j<(len(user_word)-1):
            if (secret_word[i]==user_word[j]):
                if j==i:
                    display=display+user_word[j].upper()
                correct_guest=1
            else:
                display=display+user_word[j].lower()
                correct_guest=1
            j=j+1    
        if correct_guest==0:
            display=display+'_'
        i=i+1

    print(display)