import random
import unittest

def rps():
    playerChoiceDict = {"rock" : 0, "paper" : 1, "scissors": 2}
    playerChoice = input("Rock, Paper or Scissors? ").lower().strip()

    while playerChoice not in playerChoiceDict.keys():
        playerChoice = input("Please choose either Rock, Paper or Scissors: ").lower().strip()
    
    playerChoice = playerChoiceDict[playerChoice]
    compChoice = random.randint(0, 2)
    
    print(f"Computer chose {list(playerChoiceDict.keys())[list(playerChoiceDict.values()).index(compChoice)]}...")
    print(calcRPS(playerChoice=playerChoice, compChoice=compChoice))

    playAgain = input("Would you like to play again? (y/n) ").strip()
    while playAgain != "y" and playAgain != "n":
        playAgain = input("Would you like to play again? (y/n) ").strip()

    if playAgain == "y":
        rps()
    else:
        print("Thanks for playing Rock, Paper, Scissors!")

def calcRPS(playerChoice, compChoice):
    result = playerChoice - compChoice

    if result == 0:
        return "It's a tie."
    elif result == -1 or result == 2:
        return "Computer Wins!"
    elif result == 1 or result == -2:
        return "Player Wins!"
    

def rpsls():
    playerChoiceDict = {"rock" : 0, "paper" : 1, "scissors": 2, "spock": 3, "lizard": 4}
    playerChoice = input("Rock, Paper, Scissors, Lizard or Spock? ").lower().strip()

    while playerChoice not in playerChoiceDict.keys():
        playerChoice = input("Please choose either Rock, Paper, Scissors, Lizard or Spock: ").lower().strip()
    
    playerChoice = playerChoiceDict[playerChoice]
    compChoice = random.randint(0, 4)
    
    print(f"Computer chose {list(playerChoiceDict.keys())[list(playerChoiceDict.values()).index(compChoice)]}...")
    print(calcRPSLS(playerChoice=playerChoice, compChoice=compChoice))

    playAgain = input("Would you like to play again? (y/n) ").strip()
    while playAgain != "y" and playAgain != "n":
        playAgain = input("Would you like to play again? (y/n) ").strip()

    if playAgain == "y":
        rps()
    else:
        print("Thanks for playing Rock, Paper, Scissors, Lizard, Spock!")

def calcRPSLS(playerChoice, compChoice):
    result = playerChoice - compChoice

    if result == 0:
        return "It's a tie."
    elif result == -1 or result == 2 or result == -3 or result == 4:
        return "Computer Wins!"
    elif result == 1 or result == -2 or result == 3 or result == -4:
        return "Player Wins!"

class Test(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(calcRPS(0, 0), "It's a tie.", "Rock and Rock ties")

    def test_win(self):
        self.assertEqual(calcRPS(1, 0), "Player Wins!", "Paper wins here")
        self.assertEqual(calcRPS(0, 2), "Player Wins!", "Rock wins here")
        self.assertEqual(calcRPSLS(4, 1), "Player Wins!", "Lizard wins here")
        self.assertEqual(calcRPSLS(0, 4), "Player Wins!", "Rock wins here")
        self.assertEqual(calcRPSLS(4, 3), "Player Wins!", "Lizard wins here")


    def test_loss(self):
        self.assertEqual(calcRPS(1, 2), "Computer Wins!", "Rock loses here")
        self.assertEqual(calcRPS(2, 0), "Computer Wins!", "Scissors loses here")
        self.assertEqual(calcRPSLS(0, 3), "Computer Wins!", "Rock loses here")
        self.assertEqual(calcRPSLS(4, 0), "Computer Wins!", "Lizard loses here")
        self.assertEqual(calcRPSLS(3, 4), "Computer Wins!", "Spock loses here")

if __name__ == '__main__': 
    rps()
    rpsls()   
    unittest.main()
    
