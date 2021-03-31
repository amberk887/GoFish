## /* Go Fish
## goFishCode.py
## Amber Kusma
## alkusma */

from graphics import *
import random
from random import randrange
import time
################################ Card Class ###################################################
class Card:
    def __init__(self, value):
        self.value=value ###### CLOD ######
################################ End Card Class ###############################################

############################### Cards Class ###################################################       
class Cards: ###### CLOD ######
    deck = []
    compHand = []
    playerHand = []
# creates a deck of 52 cards and calls upon the Card class to use values of each card
    def createDeck(self):
        for i in range (1,14):
            for j in range (0,4):
                if i > 1 and i < 11:
                    self.deck.append(Card(str(i)))
                elif i == 1:
                    self.deck.append(Card('A'))
                elif i == 11:
                    self.deck.append(Card('J'))
                elif i == 12:
                    self.deck.append(Card('Q')) 
                elif i == 13:
                    self.deck.append(Card('K'))
        random.shuffle(self.deck)
        return self.deck ###### LOOD ######

    def __init__(self):
        ...
# creates the hands for the comp and player using random values from the deck
    def createHand(self):
        self.compHand=[]
        self.playerHand=[]
        for i in range(0,6):
            n=randrange(0,len(self.deck))
            self.compHand.append(self.deck[n])
            self.deck.pop(n)
            n=randrange(0,len(self.deck))
            self.playerHand.append(self.deck[n])
            self.deck.pop(n)
        return self.compHand, self.playerHand

    def printCompHand(self):
        for i in self.compHand:
            print(i.value, end=" ")

    def printPlayerHand(self):
        playerHandList=[]
        for i in self.playerHand:
            playerHandList.append(i.value)
        return playerHandList

################################## End Cards Class ##############################################
#set up the graphics window, setCoords, set background color
def graphWin():  ###### GW ######
    win =GraphWin("Go Fish", 1000, 700)
    win.master.geometry('%dx%d+%d+%d' % (1000, 700, 100, 100))
    win.setCoords(0,0,10, 7)
    win.setBackground("ghostwhite")
    return win


#set up the basics of the window as well as ask the player for name, display stats, welcome to game
def firstWin(win):
    #set up the first screen
    #welcome, name box, and submit button
    #text
    ###### OTXT ######
    welcome = Text(Point(5,6), "Let's Play Go-Fish!")
    welcome.setSize(36)
    welcome.setStyle("bold")
    welcome.setTextColor("steelblue")
    enterName= Text(Point(5, 5), "Enter your name")
    enterName.setSize(20)
    enterName.setStyle("bold")
    enterName.setTextColor("steelblue")
    

    #name text box
    nameBox=Entry(Point(5,4.5),20)
    nameBox.setText(" ")

    #submit button
    submitButton = Rectangle(Point(4.5,3.75), Point(5.5,4.25))
    subButtonLabel = Text(Point(5, 4), "Submit")

    # create a list of all things that will be drawn to the window
    welcomeWindowList = [welcome, enterName, nameBox, submitButton, subButtonLabel]

    #draw all items
    for shapes in range(0,len(welcomeWindowList)):
        welcomeWindowList[shapes].draw(win)
    
    #store name when submit button is clicked
    clicked = False
    while clicked == False:
        p=win.getMouse()  ###### IMS ######
        pX=p.getX()
        pY=p.getY()
        if pX>=4.5 and pX<=5.5 and pY>=3.75 and pY<=4.25: 
            clicked = True
            ####### IEB #######
            name = str(nameBox.getText())
    return name


# reads the score file to display player's record
#takes in the name so we can see if the name is found in the scores file
def readFile(name, win):
    #open the input file
    infile=open("goFishScores.txt","r")
    #read in header
    infile.readline()
    nameFound=0
    
    # find if the player has played before
    # display their stats if they have 
    i = 0
    found = False
    infile = open("goFishScores.txt",'r')
    for line in infile:
        myData = line.split('\t')
        if myData[0].lower() == name.strip().lower():
            found = True
            wins = int(myData[1])
            losses = int(myData[2])
            ties = int(myData[3])
            record=Text(Point(8,4.5), "Your Record: ")
            record.setSize(18)
            record.draw(win)
            recordStats = Text(Point(8, 4),  " Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties) )
            recordStats.setSize(18)
            recordStats.draw(win)
        i+=1
    if found == False:
        record=Text(Point(8,4.5), "You've never played before! ")
        record.setSize(18)
        record.draw(win)

    infile.close()
        
    
# updates the score file by reading it in as an infile and writing onto the outfile     
def updateFile(win, results, name):
    scoreData=[]
    i = 0
    found = False
    infile = open("goFishScores.txt",'r')
    # goes through each line
    # if the player already exists their info will be updated if not they will have a line in the file created
    for line in infile: ###### IFL ######
        scoreData.append(line)
        myData = line.split('\t')
        if myData[0].lower() == name.strip().lower():
            found = True
            wins = int(myData[1])
            losses = int(myData[2])
            ties = int(myData[3])
            if results == "won":
                wins += 1 
            elif results == "loss":
                losses += 1
            else:
                ties += 1
            scoreData[i] = myData[0] + '\t' + str(wins) + '\t' + str(losses) + '\t' + str(ties) + '\n'
            newRecordText = Text(Point(5,3), "Your new record: ")
            newRecordText.setSize (25)
            newRecordText.draw(win)
            newRecord = Text(Point(5, 2.5),   " Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties) )
            newRecord.setSize(20)
            newRecord.draw(win)
            time.sleep(4)
        i+=1
    if found == False:
        if results == "won":
            wins, losses, ties = 1, 0, 0
        elif results == "loss":
            wins, losses, ties = 0, 1, 0
        else:
            wins, losses, ties = 0, 0, 1
        myData = [name, str(wins), str(losses), str(ties)]
        scoreData.append(name+ '\t' + str(wins) + '\t' + str(losses) + '\t' + str(ties) + '\n')
        newRecordText = Text(Point(5,3), "Your new record: ")
        newRecordText.setSize (25)
        newRecordText.draw(win)
        newRecord = Text(Point(5, 2.5),   " Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties) )
        newRecord.setSize(20)
        newRecord.draw(win)
        time.sleep(4)
    infile.close()

    outfile = open("goFishScores.txt",'w') 
    for j in range(0,len(scoreData)): ###### OFL ######
        outfile.write (scoreData[j])
    
    outfile.close()


# waits for the player to click the button to start the game                
def startGame(win):
    letsPlayButton = Rectangle(Point(4.5,2.75), Point(5.5,3.25))
    letsPlayButtonLabel = Text(Point(5, 3), "Let's Play")
    letsPlayButtonList = [letsPlayButton, letsPlayButtonLabel]
    for shapes in range (0, len(letsPlayButtonList)):
        letsPlayButtonList[shapes].draw(win)
        
    clicked = False
    while clicked == False:
        p=win.getMouse()
        pX=p.getX()
        pY=p.getY()
        if pX>=4.5 and pX<=5.5 and pY>=2.75 and pY<=3.25:
            clicked = True
    


# will draw the player's hand        
# needs to take in playerHand to know how many cards to draw as well as values
# needs to take in win to be able to draw to the graphics window
def drawGame(win, Cards, compScore, playerScore, name):
    win.close()
    win = graphWin()
    #for card in range (0, len(playerHand)):
    for i in range (1, len(Cards.playerHand)+1):
        playerCard = Image(Point(i, 1.5), "playingCard.gif")
        playerHandList=Cards.printPlayerHand(Cards)
        num=playerHandList[i-1]
        cardNum= Text(Point(i, 1.5), num)
        cardNum.setSize(30)
        cardNum.setFace("helvetica")
        cardNum.setStyle("bold")
        playerCard.draw(win)
        cardNum.draw(win)
    #for card in range (0, len(compHand)):
    for i in range (1, len(Cards.compHand)+1):
        backOfCard = Image(Point(i, 5.5), "backOfCard2.gif")
        backOfCard.draw(win)
    deckImage = Image (Point (5, 3.5), "deck.gif")
    deckImage.draw(win)
    displayScore(win, compScore, playerScore, name)

    return win


# draws the cards without displaying the score
# this is called after a goFish
def drawGameWOScore(win, Cards):
    win.close()
    win = graphWin()
    #for card in range (0, len(playerHand)):
    for i in range (1, len(Cards.playerHand)+1):
        playerCard = Image(Point(i, 1.5), "playingCard.gif")
        playerHandList=Cards.printPlayerHand(Cards)
        num=playerHandList[i-1]
        cardNum= Text(Point(i, 1.5), num)
        cardNum.setSize(30)
        cardNum.setFace("helvetica")
        cardNum.setStyle("bold")
        playerCard.draw(win)
        cardNum.draw(win)
    #for card in range (0, len(compHand)):
    for i in range (1, len(Cards.compHand)+1):
        backOfCard = Image(Point(i, 5.5), "backOfCard2.gif")
        backOfCard.draw(win)
    deck = Image (Point (5, 3.5), "deck.gif")
    deck.draw(win)
    
    return win

    
# displayScore displays each player's score in the lower right corner
def displayScore (win, compScore, playerScore, name):
    displayCompScore = Text(Point(6.5, 0.3), "Computer: "+str(compScore))
    displayPlayerScore= Text(Point(8.5,0.3), name+": "+str(playerScore))
    displayCompScore.setSize(25)
    displayPlayerScore.setSize(25)
    scoreList = [displayCompScore, displayPlayerScore]
    for shapes in range (0, len(scoreList)):
        scoreList[shapes].draw(win)
    

    
# text and text box comes up for the player to ask comp for a card    
def askForCard(win):
    #instructions
    instructions= Text(Point(5,6.5), "Ask your opponent for a card")
    instructions.setSize(22)
    
    # text box to ask for a card
    cardBox=Entry(Point(4,4.5),20)
    cardBox.setText(" ")
    
    # submit button
    submitButton = Rectangle(Point(6,4.25), Point(7,4.75))
    subButtonLabel = Text(Point(6.5, 4.5), "Submit")
    submitButton.draw(win)

    askForCardList = [instructions, cardBox, subButtonLabel]
    for shapes in range(0, len(askForCardList)):
        askForCardList[shapes].draw(win)

    
    #store asked card when submit button is clicked
    clicked = False
    while clicked == False:
        p=win.getMouse()
        pX=p.getX()
        pY=p.getY()
        if pX>=6 and pX<=7 and pY>=4.25 and pY<=4.75:
            clicked = True
            ask = str(cardBox.getText())
    return ask.upper()


# computer asks player for a card
def compsTurn(win, Cards, ask):
    if ask.value == 8 or ask.value == "A":
        question= Text(Point(3.5,4.5),"Do you have an "+str(ask.value)+"?")
        question.setSize(22)
    else:
        question= Text(Point(3.5,4.5),"Do you have a "+str(ask.value)+"?")
        question.setSize(22)

    # create yes button
    yesButton = Rectangle(Point(5,4.25), Point(6,4.75))
    yesButtonLabel = Text(Point(5.5, 4.5), "Yes")

    # create no button
    noButton = Rectangle(Point(6.5,4.25), Point(7.5,4.75))
    noButtonLabel = Text(Point(7, 4.5), "No")

    #list to draw items
    compTurnList= [question, yesButton, yesButtonLabel, noButton, noButtonLabel]
    for shapes in range (0, len(compTurnList)):
        compTurnList[shapes].draw(win)
    
    # see which has been selected
    clicked = False
    while clicked == False:
        p=win.getMouse()
        pX=p.getX()
        pY=p.getY()
        if pX>=5 and pX<=6 and pY>=4.25 and pY<=4.75:
            clicked = True
            return "yes"
        elif pX>=6.5 and pX<=7.5 and pY>=4.25 and pY<=4.75:
            clicked = True 
            return "no"
        

# will tell the player if they lost, won, or tied, and ask if they want to play again
def resultsAndPlayAgain(playerScore, compScore, win):
    win.close()
    win = graphWin()
    if playerScore>compScore:
        result = Text(Point(5, 6.5), "YOU WON!")
        result.setSize(30)
        result.draw(win)
        result = 'won'
        
    elif playerScore<compScore:
        result = Text(Point(5, 6.5), "YOU LOST!")
        result.setSize(30)
        result.draw(win)
        result = 'loss'
    else:
        result = Text(Point(5, 6.5), "YOU TIED!")
        result.setSize(30)
        result.draw(win)
        result = 'tie'

    playAgainQuest = Text(Point(5, 4.5),"Do you want to play again?")
    playAgainQuest.setSize(22)
    playAgainQuest.draw(win)
    
    # create yes button
    yesButton = Rectangle(Point(3.5,3.5), Point(4.5,4))
    yesButtonLabel = Text(Point(4, 3.75), "Yes")
    yesButton.draw(win)
    yesButtonLabel.draw(win)

    # create no button
    noButton = Rectangle(Point(5.5,3.5), Point(6.5,4))
    noButtonLabel = Text(Point(6, 3.75), "No")
    noButton.draw(win)
    noButtonLabel.draw(win)
    
        
    # see which has been selected
    clicked = False
    while clicked == False:
        p=win.getMouse()
        pX=p.getX()
        pY=p.getY()
        if pX>=3.5 and pX<=4.5 and pY>=3.5 and pY<=4:
            clicked = True
            return "yes", result, win
        elif pX>=5.5 and pX<=6.5 and pY>3.5 and pY<=4:
            clicked = True
            return "no", result, win



# takes a random card from the deck and adds it to player's hand
# deck is the full deck and hand is the player's 
def goFishPlayer(deck,hand, win):
    dt = 2
    n=randrange(0,len(Cards.deck))
    hand.append(Cards.deck[n])
    win = drawGameWOScore(win, Cards)
    goFish = Text(Point(5,6.5), "Go Fish!")
    goFish. setSize(25)
    goFish.draw(win)
    pickUpCard = Text(Point(5,6.2), "You picked up a "+str(deck[n].value))      
    pickUpCard.setSize(25)
    pickUpCard.draw(win)
    time.sleep(dt)
    Cards.deck.pop(n)
    goFish.undraw()
    pickUpCard.undraw()

    return win
    
    
# takes radndom card from deck and adds it to computer hand
def goFishComp(deck, hand, win):
    n=randrange(0,len(Cards.deck))
    hand.append(Cards.deck[n])
    win = drawGameWOScore(win, Cards)
    Cards.deck.pop(n)

    return win
    
# checks to see if the passed in hand has the value that is asked for
# if the value is found then its index is returned
# if it is not found in the list then -1 is returned
# the hand passed in is either the comp's or the player's and ask is the value in question
def checkHand(hand, ask):
    x = 0
    for i in hand:
        if ask.strip()==i.value:
            return x
        x+=1
    return -1


# will run at the very beginning of game to check for initial matches
# hand is either comp's or player's
# both hands will be checked for matches before the game starts
# the return of x will update the scores of each player
def checkMatches(hand):
    l = len(hand)
    i=x=0
    while (i < l-1):
        j = i+1
        while (j<l):
            if hand[i].value==hand[j].value:
                hand.pop(j)
                hand.pop(i)
                l=l-2
                j=l+1
                x+=1
            j+=1    
        i+=1         
    return x
                
        


# goes through the actual game: asking/ being asked for cards
# takes in the Cards class so that self.deck, self.compHand, and self.playerHand can be used
def playGame(Cards, win, name):
    # scores are set equal to the initial amount of matches
    win = drawGameWOScore(win, Cards)
    dt = 1
    checkMatchesText = Text(Point(5, 6.5), "Checking for matches...")
    checkMatchesText.setSize(20)
    checkMatchesText.draw(win)
    time.sleep(dt)
    playerScore = checkMatches(Cards.playerHand)
    compScore = checkMatches(Cards.compHand)
    moves = 0
    win = drawGame(win, Cards, compScore, playerScore, name)
    
    # will only run while both players still have cards
    while len(Cards.compHand)!=0 and len(Cards.playerHand)!=0:
        
        #when moves is even it is the player's turn so this code runs
        if moves %2 == 0 :
            ask  = askForCard(win)
            posP = checkHand(Cards.playerHand,ask)
            

##### create invalidAsk so it can be referenced wihtout error ####
            invalidAsk= Text(Point(5, 2.5),"Oops! Ask for a card you have")
            invalidAsk.setSize(20)
##################################################################
            

            # make sure the player has what they're asking for 
            if posP >= 0:
                # then checks to see if comp has the card
                # if comp has it then the card will be removed from both hands and player score will be updated
                posC = checkHand(Cards.compHand,ask)
                if posC >= 0:
                    invalidAsk.undraw()
                    Cards.compHand.pop(posC)
                    Cards.playerHand.pop(posP)
                    playerScore = playerScore + 1
                    win = drawGame(win, Cards, compScore, playerScore, name)
                    matchText = Text(Point(5, 6.5), "It's a match!")
                    matchText.setSize(25)
                    matchText.draw(win)
                    time.sleep(dt)
                    matchText.undraw()

                # if comp does not have card then goFish function will run
                # another card will be added to the player's hand and will then check to see if the new card matches existing cards
                else:
                    invalidAsk.undraw()
                    win = goFishPlayer(Cards.deck,Cards.playerHand, win)
                    playerScore+=checkMatches(Cards.playerHand)
                    win = drawGameWOScore(win, Cards)
                    displayScore(win, compScore, playerScore, name)
                    moves +=1


            # if player does not have what they asked for, they will be asked to enter a new value
            else:
                invalidAsk.draw(win)
        # comp's turn
        else :
            # random index and card will be generated for comp's turn
            n = randrange (0, len(Cards.compHand)) ###### RND ######
            ask= Cards.compHand[n]
            # player will be asked if they have the card
            answer = compsTurn(win, Cards, ask)
            check = checkHand(Cards.playerHand,ask.value)
            # if they have the card and hit the yes button-> card will be removed from both hands and comp score will update
            if (check >=0 and answer == 'yes'):
                Cards.compHand.pop(n)
                Cards.playerHand.pop(check)
                compScore = compScore + 1
                win = drawGame(win, Cards, compScore, playerScore, name)

                
            # if they have the card and hit the no button-> card will be removed from both hands, comp score will update, and player will be told they missed the card
            # this line prevents cheating
            elif (check >=0 and answer == 'no'):
                missedItText = Text(Point(5, 6.5), "You must have missed it! You do have a "+ str(ask.value))
                missedItText.setSize(25)
                missedItText.draw(win)
                time.sleep(2)
                Cards.compHand.pop(n)
                Cards.playerHand.pop(check)
                compScore = compScore + 1
                win = drawGame(win, Cards, compScore, playerScore, name)

            # if the player does not have the card then the goFish function will be called
            # comp will get a new card and then will check to see if new card matches existing cards
            else:
                win = goFishComp(Cards.deck, Cards.compHand, win)
                compScore+=checkMatches(Cards.compHand)
                win = drawGameWOScore(win, Cards)
                displayScore(win, compScore, playerScore, name)
                moves += 1
                
    return playerScore, compScore, win
    
def main():
    answer = 'yes'
    while answer =='yes':
        #set up graphics window
        win = graphWin()
        name = firstWin(win)
        # read file will find if player has played before and display stats
        readFile(name, win)
        ###### FNC ######
        startGame(win)
        c = Cards()
        deck = Cards.createDeck(c)
        Cards.compHand, Cards.playerHand = Cards.createHand(c)
        playerScore, compScore, win = playGame(Cards, win, name)
        answer, results, win = resultsAndPlayAgain(playerScore, compScore, win)
        updateFile(win, results, name)
    win.close()
            
    
main()
