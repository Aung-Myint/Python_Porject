import random
#list of Words

words=['act','apple','orange','see','solid']
word =random.choice(words)
first_time=True
answer=''
#dash display(total danses=word length)
dash_display=''
#how many letter player need to be fill
left_dash=''
#guess words by player
guess_word=''
#letter_index
current_letter_index=0
# print(len(word))
for i in range(0,len(word)):
    dash_display+='-'

left_dash=[dash_display]
# print(word)
# print(dash_display,left_dash)
while word !=answer:
    guess_letter = input("Please enter your answer letter:")
    guess_letter = guess_letter.lower()

    if(guess_letter == word[current_letter_index]):
        left_dash = list(['-'*(len(word)-(current_letter_index + 1))])
         #set guess word
        guess_word += guess_letter
         #set th answer
        answer = f'{guess_word}{left_dash[0]}'
         #show the  current incomplete answer  to display
        print(answer)
        current_letter_index +=1

    else: 
        print("wrong")
        if(first_time == True):
            first_time =False
            print('Your current status: '+ left_dash[0])
        else:
            print('Your current status'+ answer)

print(f'Your answer is {answer} and it is right!')