import random


# Takes in an arbitrary integer value and creates a dice, with roll values
# ranging from 1 to 6
class Dice():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value

    def Roll(self):
        self.value = random.randint(1, 6)
        return self


# Takes in two dice and a arbitrary sum value to create a pair of dice object
class PairDice(Dice):
    def __init__(self, die1, die2, sum):
        self.die1 = die1
        self.die2 = die2
        self.sum = sum

    def __repr__(self):
        return str(self.sum)

    def TossDie(self):
        self.die1.Roll()
        self.die2.Roll()

    def SumDie(self):
        self.sum = self.die1.value + self.die2.value
        return self.sum

    # Prints the die row by row according to the two die values passed in (ints)
    def PrintDie(self, value1, value2):
        top_bdr = " _______ "
        top = "|       |"

        inside = ["|       |", \
                  "|   *   |", \
                  "|       |", \
 \
                  "|     * |", \
                  "|       |", \
                  "| *     |", \
 \
                  "| *     |", \
                  "|   *   |", \
                  "|     * |", \
 \
                  "| *   * |", \
                  "|       |", \
                  "| *   * |", \
 \
                  "| *   * |", \
                  "|   *   |", \
                  "| *   * |", \
 \
                  "| *   * |", \
                  "| *   * |", \
                  "| *   * |"]

        bottom = "|_______|"

        print(top_bdr, end=" ")
        print(top_bdr)
        print(top, end=" ")
        print(top)
        for i in range(3):
            pat_nx = (value1 - 1) * 3 + (i)
            print(inside[pat_nx], end=" ")
            pat_ny = (value2 - 1) * 3 + (i)
            print(inside[pat_ny])
        print(bottom, end=" ")
        print(bottom)


# Initializes the two dice and the pair of dice objects
die1 = Dice(1)
die2 = Dice(1)
pairDice = PairDice(die1, die2, 2)
pairDice.TossDie()
pairDice.SumDie()

# This is the loop that creates the craps game. It has error checking for
# inputs, and keeps track of bankroll, point, bets, and whether the player has won
# or lost.
while (1):
    try:
        chips = int(input("How many chips would you like to start with?\n"))
        break
    except ValueError:
        print("Invalid number of chips\n")
while (1):
    if (chips <= 0):
        print("You're out of chips!")
        break
    while (1):
        try:
            bet = int(input("How much would you like to bet?\n"))
            break
        except ValueError:
            print("Invalid bet\n")
    if bet == 0:
        print("Play is finished\n")
        break
    elif (bet > chips):
        print("You do not have that many chips\n")
        continue
    elif (bet < 0):
        print("Invalid bet\n")
        continue
    else:
        input("Press enter to roll\n")
        pairDice.TossDie()
        sum = pairDice.SumDie()
        if (sum == 7 or sum == 11):
            pairDice.PrintDie(pairDice.die1.value, pairDice.die2.value)
            chips += bet
            print("You win! New bankroll is: ", end=" ")
            print(chips)
            print("\n")
            continue
        elif (sum == 2 or sum == 3 or sum == 12):
            pairDice.PrintDie(pairDice.die1.value, pairDice.die2.value)
            chips -= bet
            print("You lose! New bankroll is: ", end="")
            print(chips)
            print("\n")
            continue
        else:
            point = sum
            while (1):
                pairDice.PrintDie(pairDice.die1.value, pairDice.die2.value)
                print("Trying for", end=" ")
                print(point, end=" ")
                print("press enter to throw again:\n")
                input()
                pairDice.TossDie()
                sum = pairDice.SumDie()
                if (sum == point):
                    pairDice.PrintDie(pairDice.die1.value, pairDice.die2.value)
                    chips += bet
                    print("You win! New bankroll is: ", end="")
                    print(chips)
                    print("\n")
                    break
                elif (sum == 7):
                    pairDice.PrintDie(pairDice.die1.value, pairDice.die2.value)
                    chips -= bet
                    print("You lost! New bankroll is: ", end="")
                    print(chips)
                    print("\n")
                    break
                else:
                    continue