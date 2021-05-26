from random import randint
from random import shuffle

#resets everything
current_card = ""
current_cards = [0]    
current_score = 0

#creates the realistic full deck
# the ace is replaced by a 11
# jack,queen,king are accounted for
deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
shuffle(deck)
num = 4

#dealer's hand
dealer = [deck[1],deck[2]]

#introduction to game
    
print('Welcome to blackjack!')
print('Try to get to 21 without going over')
print('\n')
    

#initial 2 cards
player = [deck [3], deck[4]]
print(f'The dealer has {dealer}')  

# starting data
print(f'You hand is {player}')
score = sum(player)
print(f"the current score is {score}") 
print('\n')

#instant win condition
if score == 21:
    print('Jackpot!')
    
    
#player's turn 
while True:
    
    #lose if the score goes over 21
    if score > 21:
        print('You lose')
        print(f'You lost because your score was {score}')
        x=1
        # the x=1 stops the dealer from drawing
        break
    
    #continues if under 21
    elif score <= 21:
        hit = input('Do you want to hit it?(y/n)')
        x = 0
        # 
        if hit == 'y':
            print('hit me')
            print('\n')
            num += 1
            if deck[num] == 11 and score > 10:
                #if an ace is drawn, subtract 10 before adding it
                player.append(deck[num]-10)
                score = sum(player)
            else:
                player.append(deck[num])
                score = sum(player)

        elif hit == 'n':
            #breaks the loop and moves onto the dealer's turn
            
            print('Pass')  
            print('\n')
            break
        
        else:
            #retry if the player enters an invalid answer    
            
            print('Try again')
            print('\n')
            continue
            
            
            
    #recap on the current score        
    print('\n')
    print(f'You hand is {player}')
    print(f"the current score is {score}")
    print('\n')

# Dealer's turn to draw, as long as you didn't already lose
while x == 0:
    d_score = sum(dealer)
    if d_score > 21:
        print(f"You won, because the dealer's score was {d_score}") 
        print(f' The dealer had {dealer}')
        x = 2
        break
    
    # stops picking cards if the dealer's score goes pass 18
    elif d_score >17:
            print (f" The dealer's score was {d_score}")
            print(f' The dealer had {dealer}')     
            break
    # continues picking cards to get to 21        
    elif d_score < 21:
        num += 1
        
        if deck[num] == 11 and d_score > 10:
                #if an ace is drawn, subtract 10 before adding it
                dealer.append(deck[num]-10)
                score = sum(player)
                
        else:
            dealer.append(deck[num])
            d_score = sum(dealer)
            
            
    
#check who won as long as no one immediately lost 
while x ==0:
    if d_score > score:
        print('You lose')
        print(f' Player :{score}, dealer:{d_score}')
        print('\n')
        break
    elif d_score == score:
        print('Tie!')
        print(f' Player :{score}, dealer:{d_score}')
        break
    else:
        print('You win!')
        print(f' Player :{score}, dealer:{d_score}')
        print('\n')
        break