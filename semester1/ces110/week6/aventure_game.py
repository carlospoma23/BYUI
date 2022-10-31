print('welcome to the Aventure Game')
print('_______________________________')
print('As an avid traveler, you have decided to visit and explore the jungle located ')
print('in eastern Peru. However, while exploring it, he finds himself lost. You have to choose')
print('which direction to continue. LEFT/RIGHT/FORWARD. ')

direction= input("Which direction will you choose? ")

if(direction.lower()=='left'):
    print('As you walk, you notice a giant anaconda slowly approaching you.') 
    act= input("You're scared, What would you like to do? RUN or FIGHT.?")
    if(act.lower()=='run'):
        print("Good Job!,  This anaconda was injured and could not have reached you. ")
        print("You're still alive! continue like this.")
        
    else:
        print("Bad decision, even though the anaconda is alive but can still hurt you.")
        print('you are scared but since the anaconda is bleeding and you decided to fight so you can do it so you look in your bag,')
        print('a PISTOL that only has one bullet or a CROSSBOW With many arrows, which users?')
        act2=input('choose the weapon you will use (GUN/CROSSBOW)')
        if (act2.lower==('pistola')):
            print('bad luck, the anaconda will get shot, however, it will still have the strength to chase you. Run!')
        else:
            print('After many shots with the arrows you manage to kill the anaconda. You are still alive and after so many screams, other people manage to hear you and you return home.')



elif(direction.lower()=='right'):
    print('As you walk it gets dark and you hear the roar of a Panther and it walks towards you.')
    act= input("You're scared, What would you like to do? HIDE or CLIMB.?")
    if(act.lower()=='climb'):
        print("Good Job!,  The panther is not good at climbing trees.")
        print("You're still alive! continue like this.")
    else:
        print("Bad decision, the panther has a good sense of smell and can see in the dark, possibly it can hurt you.")
        print('You are so scared but you can see that the panthera is not very big and that it is injured.')
        print(' the panther manages to see you so you must FIGHT or RUN')
        act2=input(' what do you decide? FIGHT/RUN ')
        if (act2.lower==('fight')):
            print('Good choice, you manage to beat the panthera, after 1 hour other people manage to find you')
        else:
            print('After a few hours of running, you realize that the panthera is no longer following you but you are very tired, thirsty and hungry.')

elif(direction.lower()=='forward'):
    print('As you walk, you reach the shore of the Amazon River, but since you know how to swim,')
    print('you think you can swim across it. You are not afraid anymore, but you think it would be')
    print('nice to find some wood and build a small boat,')
    act= input('what would you like to do? SWIMMING or BUILDING. :')
    
    if(act.lower()=='building'):
        print("Good Job!,  Building a boat and sailing down the Amazon will help you find a way out quickly.")
        print("You're still alive! continue like this.")
        print('You consider that it would be ideal to approach the shore but the boat is moving very fast.')
        act2=input(' what do you decide? GO/STOP ')
        if (act2.lower==('stop')):
            print('Bad choice, now you will be a prisoner of a tribe, and they are cannibals. end of the story')
        else:
            print('Good choice, Those people belong to a tribe, a tribe of cannibals, and they could have done you a lot of harm.')
            print('Soon you will find a good port and you will be safe.')
    else:
        print("Bad decision, The Amazon River is apparently very calm, but it is actually a very dangerous river.")
        
        
        