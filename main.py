import random
from pyfiglet import Figlet, print_figlet
import time

def HigherOrLower():
  f = Figlet(font='slant')
  print("Opening...")
  time.sleep(0.5)
  print("You Have To Guess The Number From 1, To 100! You Have Unlimited Tries")
  print("You Time Starts.. ")
  time.sleep(0.3)
  print("NOW")
  guesses = 0
  randomnumber = random.randint(1,100)
  while 1 == 1:
    guess = int(input("What is you'r guess:\n"))
    if guess == randomnumber:
      print(f.renderText('WINNER'))
      time.sleep(0.5)
      print(f.renderText('WINNER'))
      time.sleep(0.5)
      print(f.renderText('------'))
      print(f.renderText('You Took '+str(guesses)+' Tries!'))
      print(guesses)
      break
    elif guess > randomnumber:
      print(f.renderText('Too High!'))
      print(f.renderText('------'))
      guesses += 1
    elif guess < randomnumber:
      guesses += 1
      print(f.renderText('Too Low!'))
      print(f.renderText('------'))



def RockPaperScissors():
  aichoice = random.randint(1,3)
  f  = Figlet(font='slant')
  ## 1 == Rock, 2 == Paper, 3 == Scissors
  print("You Have 3 Choices, Rock, Paper, Scissors... I Wish you luck...")
  while 1 == 1:
    playerChoice = input("What Will Be You'r Choice?:\n")
    if playerChoice == "Rock":
      if aichoice == 1:
        print(f.renderText('DRAW!'))
        print("The Ai Chose Rock")
        break
      elif aichoice == 2:
        print(f.renderText('You Lost!'))
        print("the Ai Chose Paper")
        break
      elif aichoice == 3:
        print(f.renderText('WINNER!'))
        print("The Ai Chose Scissors")
        break
    elif playerChoice == "Paper":
      if aichoice == 1:
        print(f.renderText('WINNER'))
        print("The Ai Chose Rock")
        break
      elif aichoice == 2:
        print(f.renderText('DRAW'))
        print("The Ai Chose Paper")
        break
      elif aichoice == 3:
        print(f.renderText('You Lost!'))
        print("The Ai Chose Scissors")
        break
    elif playerChoice == "Scissors":
      if  aichoice ==  1:
        print(f.renderText('You Lost!'))
        print("The Ai Chose Rock")
        break
      elif aichoice == 2:
        print(f.renderText('WINNER'))
        print("The Ai Chose Paper")
        break
      elif aichoice == 3:
        print(f.renderText('DRAW'))
        print("The Ai Chose Scissors")
        break
    else:
      print("Sorry, We Could Not UnderStand You'r Input")
      print("Restarting")
      time.sleep(0.5)


