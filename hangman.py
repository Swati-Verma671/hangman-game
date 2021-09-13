#Hangman project
import random

lst = list()
lst=["apple","apricot",
"avocado",
"banana",
"blackberry",
"blackcurrant",
"blueberry",
"cactuspear",
"cherimoya",
"cherry",
"chicofruit",
"coconut",
"crabapple",
"cranberry",
"currant",
"date",
"dragonfruit",
"durian",
"eggfruit",
"fig",
"grape",
"grapefruit",
"guava",
"huckleberry",
"jackfruit",
"kiwi",
"lemon",
"lime",
"lychee",
"mango",
"melon",
"mulberry",
"nectarine",
"orange",
"papaya",
"peach",
"pear",
"plum",
"pineapple",
"plumcot",
"pomegrenate",
"raspberry",
"redcurrant",
"strawberry",
"tamarind"
]

word=random.choice(lst)

print(word)
#initializing
missedletter=""
turns=len(word)

#starting off
print("Hello! Welcome to the hangman game.\n")
name=input("Please give your good name: ")
print("We hope you have a good time!!",name)

#empty string to store the results
empty=""

#the loop
while(turns>0):
    failed=0
    #checks the secret word.
    for char in word:
        #checks if the character is present in the empty string.
        if char in empty:
            print(char)
            
            
        else:
            print("_")
            failed+=1
    if(failed==0):
        print("Congratulations! You won the game.")
        break    
               

    guess=input("Please enter a letter: ")
    if(guess.isalpha()==False):
        print("Please enter a LETTER.\n")
        continue
    #adds the user's guess in the empty string.
    empty+=guess
    #checks if the user's guess is in secret word.
    if guess not in word:
        turns-=1
        missedletter+=guess
    #checks the number of turns.    
    if turns==0:
        print("You, have unfortunately lost, the word was :",word)
        break
    

    print("Missed Letter: ",missedletter)

    
    


    
        

    
        
        

        


    
    














