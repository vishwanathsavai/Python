import random


def create_deck():
    for suit in SUITS:
        for pip in PIPS:
            card = (suit,pip)
            deck.append(card) 




def deal_deck():
    card = random.choice(deck) 
    deck.remove(card)
    return card

def deal_check(player,deck_list):
    card = player
    deck_list.remove(card)
    print("In deal_check {}".format(card))
    return card

def user_select():
    return random.randint(0,1)
    

def put_card(deck_list,random_card):
    flag = 0
    for d in deck_list:
        d_pip,d_suit = d
        ran_pip,ran_suit = random_card[-1]
        print("match selected {} and {}".format(d_suit,ran_suit))
        if ran_suit == d_suit:
            print("in put card")
            print("match selected {} \n {}".format(d_suit,ran_suit))
            random_card.append(deal_check(d,deck_list))
            flag =1
    return flag

'''def series_check(system_deck,random_card):
    for d in range(0,len(system_deck)):
        d_pip,d_suit = d
        
        ran_pip,ran_suit = random_card[-1]
        if ran_suit == d_suit:
            if d_suit'''
            
def drop_other_commons(system_deck,random_card):
    flag = 0
    try:
        for d in range(0,len(system_deck)):
            d_pip,d_suit =  system_deck[d]
            for e in range(d,len(system_deck)):
                e_pip,e_suit = system_deck[e]
                if d != e and d_suit==e_suit and e_pip!=d_pip:
                    print("In drop commons")
                    random_card.append(deal_check(system_deck[e],system_deck))
                    random_card.append(deal_check(system_deck[d],system_deck))
                    flag = 1
    except IndexError:
        print("Match was found so that value was deleted")
        
    if flag == 0:
        print("In max drop check")
        for d in system_deck:
            d_pip,d_suit = d
            if d_suit=="K" or d_suit == "Q" or d_suit == "J" or d_suit == "10" or d_suit == "9":
                random_card.append(deal_check(d,system_deck))
                flag = 1
                break
            elif d_suit == "8" or d_suit == "7" or d_suit == "5":
                random_card.append(deal_check(d,system_deck))
                flag = 1
                break
            elif d_suit == "4" or d_suit == "3" or d_suit == "2" or d_suit == "A":
                random_card.append(deal_check(d,system_deck))
                flag = 1
                break
            
def draw_a_card(list1):
    list1.append(deal_deck())
    
def series_card(list_deck,random_card):
    ser_list=[]
    check_list = []
    counter = 0
    for x in range(0,len(list_deck)):
        x_pip,x_suit = list_deck[x]
        check_list.extend(list_deck[x])
        for y in range(0,len(list_deck)):
            y_pip,y_suit = list_deck[y]
            if(x!=y):
                check_list.extend(list_deck[y])
        print("Series cards selected are")
        print(check_list)
        check_list.clear()
                    
    
    '''for i in ser_list:
        pip,suit = i
        print(suit + pip, end = " ")
        print("\n")'''

            
                
                
                
        

CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"

PIPS = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
SUITS = (CLUB, SPADE, DIAMOND, HEART)

deck = [] 

create_deck() 
#deal_deck() 

USER = 0
SYSTEM = 1
PLAYERS = (USER,SYSTEM)
user_deck = []
system_deck = []
for i in range(0,5):
    user_deck.append(deal_deck())

for i in range(0,5):
    system_deck.append(deal_deck())

print("LET THE GAME BEGIN\n")
#print(deck)

random_card = []
random_card.append(deal_deck())

for ran in random_card:
    pip,suit = ran
    print(suit + pip, end = " ")
print("\n")
user_deck.sort(reverse = True)
system_deck.sort(reverse = True)

print("User deck")    
for i in user_deck:
    pip,suit = i
    print(suit + pip, end = " ")
print("\n")
print("system deck")
for i in system_deck:
    pip,suit = i
    print(suit + pip, end = " ")
print("\n")   
print("\n")

#selecting random card's pip and suit


#print(ran_suit)
deal = True
select = user_select()
while deal:
    if (select == 0):
        print("Its Your turn to go ahead first")
        for i in user_deck:
            pip,suit = i
            print(suit + pip, end = " ")
        print("Which Card from above set do you want to put")
        #check if value put to random is common to randon if yes then done draw any from deck 
        #if no then draw a card # if possible check for the conditions if its satisfing or not.
        sel_list = []
        axis = True
        print(len(user_deck))
        while axis:
            try:
                ch = int(input("Select Index value and click enter press any character to exit: "))
                if ch <=len(user_deck):
                    sel_list.append(user_deck[ch])
                else:
                    print("Select some other value lesser than {}" .format(len(user_deck)))
            except:
                print("Done with your selects")
                axis = False
        print(sel_list)
            
    
    else:
        print("Its System's turn\n")
        #if series_card(system_deck,random_card):
            #print("Series of cards has been dropped")
        if put_card(system_deck,random_card):
            print("common")
        else:
            drop_other_commons(system_deck,random_card)
            (system_deck)
    if(select == 1):
        select = 0
    else:
        select = 1
    deal = False
        

            
for ran in random_card:
    pip,suit = ran
    print(suit + pip, end = " ")
print("\n")

for i in user_deck:
    pip,suit = i
    print(suit + pip, end = " ")
print("\n")
print("system deck")
for i in system_deck:
    pip,suit = i
    print(suit + pip, end = " ")
print("\n") 
