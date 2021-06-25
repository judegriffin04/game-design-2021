#jude griffin
#final project
#6/23/21
#This project is an expansion of the word guessing game we made earlier in the class. I wanted to give it a lot more variety and difficulty
import random
myEasyWords = ['cat', 'dog', 'car', 'hat', 'bat', 'rat', 'door', 'house', 'train', 'city', 'open', 'close']
myColors = ['blue', 'red', 'pink', 'green', 'brown', 'yellow', 'purple', 'beige', 'indigo', 'violet', 'orange', 'white', 'black']
myNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
myFruits = ["apples", "raspberries", "bananas", "apricots", "pears", "dragonfruit", "passionfruit", "watermelon", "grapes" ]
techWords = ['python', 'java', 'trackpad', 'computer', 'keyboard', 'geeks', 'laptop', 'headphones', 'charger', 'mouse', 'software', 'hardware']
countryWords = ['canada', 'china', 'mozambique', 'kenya', 'mexico', 'ireland', 'india', 'myanmar', 'laos', 'vietnam', 'hungary', 'italy', 'benin', 
'egypt', 'france', 'spain', 'sweden', 'japan', 'zambia', 'zimbabwe', 'mongolia', 'maldives', 'australia', 'fiji', 'venezuela', 'brazil', 'portugal',
 'greece', 'pakistan', 'thailand', 'bangladesh', 'malaysia', 'singapore', 'peru', 'colombia', 'haiti', 'jamaica', 'uruguay', 'paraguay', 'dominica', 'cuba', 'germany', 'poland']
myElements = ['actinium', 'aluminium', 'antimony', 'argon', 'arsenic', 'astatine', 'barium', 'beryllium', 'bismuth', 'boron', 'bromine', 'cadmium', 'calcium', 'carbon', 'cerium',
'cesium', 'chlorine', 'chromium', 'cobalt', 'copper', 'dysprosium', 'erbium', 'europium', 'fluorine', 'francium', 'gadolinium', 'gallium', 'germanium', 'gold', 'hafnium', 'helium', 
'hydrogen', 'indium', 'iodine', 'iridium', 'iron', 'krypton', 'lanthanum', 'lead', 'lithium', 'lutetium', 'magnesium', 'manganese', 'mercury', 'molybdenum', 'neodymium', 'neon', 'nickel', 
'niobium', 'nitrogen', 'osmium', 'oxygen', 'palladium', 'phosphorus', 'platinum', 'polonium', 'potassium', 'promethium', 'protactinium', 'radium', 'radon', 'rhenium', 'rhodium', 'rubidium', 
'ruthenium', 'samarium', 'scandium', 'selenium', 'silicon', 'silver', 'sodium', 'strontium', 'sulfur', 'tantalum', 'tellurium', 'terbium', 'thorium', 'thallium', 'tin', 'titanium', 'tungsten', 'uranium', 'vanadium', 'xenon', 'ytterbium', 'yttrium', 'zinc', 'zirconium']
name = input("What is your name: ")
score = 0
score0 =0 #score is universal across all levels so it has to be before the while loop
totalCorrectGuesses =0 #keeps track of the player's total guessed letters to be shown along with the score
totalIncorrectGuesses =0
var = True
while var:
    print("-"*15)
    print("  Welcome,", name)
    print("     to the")
    print("Word Guessing Game!")
    print(" Choose your stage:")
    print("  1. Very Easy") #scaling difficulty in two ways: word length/complexity and number of turns. you have the fewest guesses to get the hardest words so it should be a serious challenge
    print("  2. Easy") #each difficulty has multiple indexes it can choose a word from, raising the difficulty by making it harder to memorize all the words
    print("  3. Normal")
    print("  4. Hard") #each difficulty level has 2 less turns than the last
    print("  5. Very Hard") #each difficulty gives you a different amount of points for winning
    print("  6. Sudden Death Mode") #uses all possible indexes, and you cannot have an incorrect guess
    print("  7. Scores") #shows wins, incorrect letter guesses, and correct letter guesses
    print("  8. Word Key") #shows all the possible words
    print("  9. End Game")
    print("-"*15)
    choice = input("What will you do?: ")
    if choice == "1":
        word1 = random.choice(myEasyWords + myColors + myNumbers)
        counter1 = len(word1)
        turns1 = 10 
        guesses1 = ' '
        while turns1>0 and counter1 >0:
            for char in word1:
                if char in guesses1:
                    print(char,end = ' ')
                else:
                    print("_",end=' ')
            newGuess1=input("\n\n Guess a letter: ")
            if newGuess1 not in guesses1:
                if newGuess1 not in word1:
                    turns1 -= 1
                    totalIncorrectGuesses += 1
                    print("Sorry, guess again! You have", turns1, "remaining." )
                else:
                    counter1 -= word1.count(newGuess1)
                    guesses1 += newGuess1
                    totalCorrectGuesses += 1
            else:
                print("You already guessed that!")
            if counter1 == 0:
                score0 += 1
                score += 1
                print(word1)
                print("Congrats! You win!")
                print("Score:", score0)
            else:
                if newGuess1 not in word1: #without this it will print 'Try Again!' after every guess
                    if turns1>0:
                        print("Try again!")
                    else:
                        while True:
                            print("You failed!")
                            break
    if choice == "2":
        word2 = random.choice(myNumbers + myFruits)
        counter2 = len(word2) #each level has its own variables so things dont get mixed up
        turns2 = 8
        guesses2 = ' '
        while turns2>0 and counter2 >0:
            for char in word2:
                if char in guesses2:
                    print(char,end = ' ')
                else:
                    print("_",end=' ')
            newGuess2=input("\n\n Guess a letter: ")
            if newGuess2 not in guesses2:
                if newGuess2 not in word2:
                    turns2 -= 1
                    totalIncorrectGuesses += 1
                    print("Sorry, guess again! You have", turns2, "remaining." )
                else:
                    counter2 -= word2.count(newGuess2)
                    totalCorrectGuesses += 1
                    guesses2 += newGuess2
            else:
                print("You already guessed that!")
            if counter2 == 0:
                print(word2)
                print("Congrats! You win!")
                score0 += 1
                score +=2
            else:
                if newGuess2 not in word2:
                    if turns2>0:
                        print("Try again!")
                    else:
                        while True:
                            print("You failed!")
                            break 
    if choice == "3":
            word3 = random.choice(myFruits + techWords)
            counter3 = len(word3)
            turns3 = 6
            guesses3 = ' '
            while turns3>0 and counter3 >0:
                for char in word3:
                    if char in guesses3:
                        print(char,end = ' ')
                    else:
                        print("_",end=' ')
                newGuess3=input("\n\n Guess a letter: ")
                if newGuess3 not in guesses3:
                    if newGuess3 not in word3:
                        turns3 -= 1
                        totalIncorrectGuesses += 1
                        print("Sorry, guess again! You have", turns3, "remaining." )
                    else:
                        counter3 -= word3.count(newGuess3)
                        totalCorrectGuesses += 1
                        guesses3 += newGuess3
                else:
                    print("You already guessed that!")
                if counter3 == 0:
                    print(word3)
                    print("Congrats! You win!")
                    score0 += 1
                    score += 3
                else:
                    if newGuess3 not in word3:
                        if turns3>0:
                            print("Try again!")
                        else:
                            while True:
                                print("You failed!")
                                break       
    if choice == "4":
            word4 = random.choice(techWords + countryWords)
            counter4 = len(word4)
            turns4 = 4
            guesses4 = ' '
            while turns4>0 and counter4 >0:
                for char in word4:
                    if char in guesses4:
                        print(char,end = ' ')
                    else:
                        print("_",end=' ')
                newGuess4=input("\n\n Guess a letter: ")
                if newGuess4 not in guesses4:
                    if newGuess4 not in word4:
                        turns4 -= 1
                        totalIncorrectGuesses += 1
                        print("Sorry, guess again! You have", turns4, "remaining." )
                    else:
                        counter4 -= word4.count(newGuess4)
                        totalCorrectGuesses += 1
                        guesses4 += newGuess4
                else:
                    print("You already guessed that!")
                if counter4 == 0:
                    print(word4)
                    print("Congrats! You win!")
                    score0 += 1
                    score += 4
                else:
                    if newGuess4 not in word4:
                        if turns4>0:
                            print("Try again!")
                        else:
                            while True:
                                print("You failed!")
                                break            
    if choice == "5":
            word5 = random.choice(countryWords + myElements)
            counter5 = len(word5)
            turns5 = 2
            guesses5 = ' '
            while turns5>0 and counter5 >0:
                for char in word5:
                    if char in guesses5:
                        print(char,end = ' ')
                    else:
                        print("_",end=' ')
                newGuess5=input("\n\n Guess a letter: ")
                if newGuess5 not in guesses5:
                    if newGuess5 not in word5:
                        turns5 -= 1
                        totalIncorrectGuesses += 1
                        print("Sorry, guess again! You have", turns5, "remaining." )
                    else:
                        counter5 -= word5.count(newGuess5)
                        totalCorrectGuesses += 1
                        guesses5 += newGuess5
                else:
                    print("You already guessed that!")
                if counter5 == 0:
                    print(word5)
                    print("Congrats! You win!")
                    score0 += 1
                    score += 5
                else:
                    if newGuess5 not in word5:
                        if turns5>0:
                            print("Try again!")
                        else:
                            while True:
                                print("You failed!")
                                break            
    if choice == "6":
            word6 = random.choice(myEasyWords + myColors + myNumbers + myFruits + techWords + countryWords + myElements)
            counter6 = len(word6)
            turns6 = 1
            guesses6 = ' '
            while turns6>0 and counter6 >0:
                for char in word6:
                    if char in guesses6:
                        print(char,end = ' ')
                    else:
                        print("_",end=' ')
                newGuess6=input("\n\n Guess a letter: ")
                if newGuess6 not in guesses6:
                    if newGuess6 not in word6:
                        turns6 -= 1
                        totalIncorrectGuesses += 1
                        print("Sorry, guess again! You have", turns6, "remaining." )
                    else:
                        counter6 -= word6.count(newGuess6)
                        totalCorrectGuesses += 1
                        guesses6 += newGuess6
                else:
                    print("You already guessed that!")
                if counter6 == 0:
                    print(word6)
                    print("Congrats! You win!")
                    score0 += 1
                    score +=6
                else:
                    if newGuess6 not in word6:
                        if turns6>0:
                            print("Try again!")
                        else:
                            while True:
                                print("You failed!")
                                break            
    if choice == "7":
        print("- "*42)
        print("  Scoreboard:")
        print(name,":", score, "Points,", score0, "Words Guessed,", totalCorrectGuesses, "Letters Guessed,", totalIncorrectGuesses, "Incorrect Letter Guesses.")
        print("- "*42)
    if choice == "8":
        print("- "*60)
        print(" ")
        print("WORD KEY")
        print(" ")
        print("Easy words:", myEasyWords)
        print(" ")
        print("Colors", myColors)
        print(" ")
        print("Numbers", myNumbers)
        print(" ")
        print("Fruit", myFruits)
        print(" ")
        print("Tech", techWords)
        print(" ")
        print("Countries", countryWords)
        print(" ")
        print("Elements", myElements)
        print("- "*50)
    if choice == "9":
        print("Goodbye! Thanks for playing!")
        var = False
