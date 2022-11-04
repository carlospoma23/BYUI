import random
list_words=['mosiah','helaman','moroni','abinadi','samuel','lehi','benjamin']
secret_word=random.choice(list_words)


index=0
count=0
repetidos=[]
for i in secret_word:
    if(i.isalpha()):
        if(secret_word==secret_word[index]):
            index+=1
            count+=1

print(f'The word is {secret_word} and the {count}')
        

"""
This is working
letter='a'

index=0
count=0

for j in secret_word:
    if (letter==secret_word[index]):
        count+=1
    print(secret_word[index])
        
    index+=1

print(f"La letra {letter} se repite {count} veces en la palabra {secret_word}")



"""





"""

print("Comienzo")
index=0
for j in secret_word:
    letter=secret_word
    print(f" My index is {index} and {secret_word[index]} {j} {letter}")
    index+=1
print(secret_word[0])

"""
