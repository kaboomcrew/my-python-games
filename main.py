import random
from pyfiglet import Figlet, print_figlet
import time
import split
from random import shuffle

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

def unscrambleGame():
  f = Figlet(font="slant")
  print("You Will Have to Guess the unscrambled word, You Have 5 tries!")
  ## to add works put strings in the list below
  num1 = ["Kaboom", "Python", "Game", "Lua", "JavaScript", "Websites", "GitHub"]
  num1 = random.choice(num1)
  num1 = num1.lower()
  word = list(num1)
  shuffle(word)
  print(''.join(word))
  tries = 0
  while 1 == 1:
    if tries == 5:
      print("You Ran Out Of Tries!")
      break
    else:
      userawnser = str(input("You'r Answer:\n"))
      tries += 1
      if userawnser == num1:
        print(f.renderText('WINNER'))
        time.sleep(0.5)
        print(f.renderText('WINNER'))
        print("You took "+str(tries)+" Tries!")
        break
      else:
        print("Nope")


def mathematicas():
  font = Figlet(font="slant")
  firstnum = random.randint(1,100)
  secnum = random.randint(1,100)
  totalnum = firstnum + secnum
  print("What is "+str(firstnum)+" + "+str(secnum)+"?")
  plrguess = int(input(""))
  if plrguess == totalnum:
    print(font.renderText("CORRECT"))
    print("Correct")
  else:
    print(font.renderText("INCORRECT"))
    print("Incorrect")




