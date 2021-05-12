from random import randint
name = input('What is your name? : ')
x = randint(1,101)
dict = {
        'a':'You are FREEZING!', 
        'b':'You are getting colder :(',
        'c':'You are getting warmer :)',
        'd':'You are BURNING!',
        'e':'That answer was: Cold!',
        'f':'That answer was: Warm!',
        'g':'LOL you chose the same number, too bad!'
       }


print('Welcome to the guesssing game!')
print('\n')
print("The rules are simple, guess a number between 1-100 and we'll tell you if you're cold or warm!")
print("If you get really close or really far, we'll tell you BURNING OR FREEZING")
print('We will also tell you if you are getting colder or warmer')
print('You get 10 tries before you lose the game!')
print(f'Good luck {name}!')
print('\n')
      
guesses = [0]

while True:
    y=int(input('Choose a number between 1-100: '))
    
    if y > 100 or y < 0:
        print('Out of bound, please try again')
        print('\n')
        continue
        
    guesses.append(y)
    print(f"The previous 3 guesses you've made are {guesses[-4:-1]}")
    print(f'You have {11-len(guesses)} tries remaining.')
    
    if y == x:
        break
    
    if abs(y-x) > 20:
        print(dict['a'])
        
        if guesses[-2] == 0:
            pass
        elif abs(guesses[-2]-x) < abs(y-x):
            print(dict['b'])
        elif abs(guesses[-2]-x) >= abs(y-x):
            print(dict['c'])
        print('\n')
        
    elif abs(y-x)<=5:
        print(dict['d'])
        
        if guesses[-2] == 0:
            pass
        elif abs(guesses[-2]-x) < abs(y-x):
            print(dict['b'])
        elif abs(guesses[-2]-x) >= abs(y-x):
            print(dict['c'])
        print('\n')
    
    elif abs(y-x) > 10:
        if guesses[-2] == 0:
            pass
        else:
            print(dict['e'])
        if (guesses[-2]-x) == (y-x):
            print(dict['g'])
        elif abs(guesses[-2]-x) < abs(y-x):
            print(dict['b'])
        elif abs(guesses[-2]-x) > abs(y-x):
            print(dict['c'])
        print('\n')
        
    elif abs(y-x)<=10:
        if guesses[-2] == 0:
            pass
        else:
            print(dict['f'])
        if (guesses[-2]-x) == (y-x):
            print(dict['g'])
        elif abs(guesses[-2]-x) < abs(y-x):
            print(dict['b'])
        elif abs(guesses[-2]-x) >= abs(y-x):
            print(dict['c'])

        print('\n')
        
    if len(guesses) == 10:
        print(f'You lose! The random number was {x}!')
        break
        
print (f'Congrats! You won! The random number was {x}!')