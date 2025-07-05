print("😍 --------------------------------- 😍")  
print("")
print("😍 ~~~~~~~~~~ welcom to RPS ~~~~~~~ 😍")

# 
read_file = open("word.txt","r")
a = read_file.readline()
words = a.split(",")
print(words)
# 

import random
# words = ["ironman","thor","hawkeye","wanda","vision"]
word = random.choice(words)
print(word)
jumble = "".join(random.sample(word, len(word)))
print(jumble)

chances = 3
print("~"*30)
print("----Avengers Jumble Bumble-----")
print("~"*30)

while chances != 0:
    print("the word is ", jumble)
    
    guess = input("enter your geussd word: ").lower()
    if guess == word:
        print("Correct Guess!!")
        print("You won!")
        print(" ")
        break
    else:
        chances -= 1
        print("Incorrect Guess!!")
        print("Remaining chances are:", chances)
        print()
else:
    print("all you chances are exhausted")
    print("You lose")

print("Thank you for playing the game!!")
               