# 🎲 Word Scrambler Game
# Author: hajar1010
# Description: Scrambles a word and asks the user to guess the original.

import random
print("heyy wanna play a fun game ??!!")
print("I'll scramble a word and you have to guess the original word ")

score=0
while True :
# Define a list of words to choose from
    my_list= ["python", "banana", "coding", "giraffe", "keyboard","whiteborad","television","functions","school","capebara","coding", "planet", "rocket", "window", "coffee", "laptop","umbrella", "elephant", "backpack", "triangle", "notebook", "sandwich", "building", "airplane", "reptile", "calendar","awkward", "rhythm", "pneumonia", "jazz", "zodiac", "mystery", "phantom", "illusion", "treasure", "blizzard"]
#Pick a random word from the list
    word=random.choice(my_list)
# Scramble the letters of the word
    my_word=list(word)
    random.shuffle(my_word)
    print('________________________________________')
    print("ohh i got you the best word!!")
#Show the scrambled word to the user
    scrambled = ''.join(my_word)
    print("here is the scrambled word : " ,scrambled)
#Ask the user to guess the original word
    print('________________________________________')
    user_word=input("can you guess the original word buddy \n what you got in mind : ")
#Check if the guess is correct
    print('________________________________________')
    if user_word== word:
        score+=10
        print("BINGOO!!you got it right, your score is : ",score)
    else:
        print("oh ohh you screwed up , your score is : ",score)
# 8. Ask the user if they want to play again
    response=input("that was fun wanna play again ?? yes or no ")
    if response == "yes":
        print("suure you got itt")
        continue
    else :
        print("alrightt")
        break
# 10. Say goodbye and show final score
print("well that was a good game")
