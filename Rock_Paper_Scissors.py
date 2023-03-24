from random import choice
#options that computer and player 
options = ['rock', 'paper', 'scissor']
# computer random choice
player_choice = " "

while (player_choice != "exit") :

    computer_choice = choice(options)
    # player chice from input (make sure to lower the letter)
    player_choice = input('What is your choice? rock,paper,scissor ').lower()
    # if player are not in options
    if player_choice not in options:
        print('Out of options')
    else:
        if player_choice == computer_choice:
            print('Tie!')
        else:
            if player_choice == 'rock':
                if computer_choice == 'paper':
                    print('Your lose, Computer '+ computer_choice+ 'covers player '+ player_choice)
                else:
                    print('You Win, player '+ player_choice + 'beats computer '+ computer_choice)
            
            if player_choice == 'paper':
                if computer_choice == 'scissor':
                    print('Your lose, Computer '+ computer_choice+ 'cuts player '+ player_choice)
                else:
                    print('You Win, player '+ player_choice + 'cover computer '+ computer_choice)
            
            if player_choice == 'scissor':
                if computer_choice == 'rock':
                     print('Your lose, Computer '+ computer_choice+ 'beats player '+ player_choice)
                else:
                    print('You Win, player '+ player_choice + 'cuts computer '+ computer_choice)
            


    
        

# print('Computer :' + computer_choice)
# print('player :'+ player_choice)