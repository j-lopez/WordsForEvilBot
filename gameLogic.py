from gameboardGraph import gameboardGraph
from time import sleep
from imageProcessing import grabImage
from pytesseract import image_to_string
from pyautogui import position, press, typewrite, keyUp, keyDown
import random

def wordSearch(t, g):

    def recursiveSearch(tile, word, trie):
        path = word + tile.value

        tile.used = True
        foundWords = []

        if trie.search(path):
            foundWords.append(path)
        neighbors = [n for n in tile.neighbors if not n.used]
        trieChildren = trie.getChildren(path)

        for n in neighbors:

            letter = 0

            if (n.value == "QU"):
                letter = ord("Q") - ord('A')
            else:
                letter = ord(n.value) - ord('A')

            if trieChildren:

                if letter < 0 or letter > 25:
                    return foundWords

                if trieChildren[letter]:
                    foundWords.extend(recursiveSearch(n, path, trie))

        tile.used = False

        return foundWords


    # Graph data structure and all methods

    if g.setGameboard():
        allWords = []

        for line in g.board:
            for node in line:
                allWords.extend(recursiveSearch(node, '', t))

        recommended = sorted(allWords, key=len)

        g.words = list(set(recommended[-5:]))
        g.words.reverse()

        return "Words found"

    else:
        return "None found"

def treasure(t, board):

    letters = []

    for i in range(5):
        letters.append([board[0][i], board[1][i]])

    for i1 in range(2):
        for i2 in range(2):
            for i3 in range(2):
                for i4 in range(2):
                    for i5 in range(2):
                        word = letters[0][i1] + letters[1][i2] + letters[2][i3] +  letters[3][i4] + letters[4][i5]
                        if t.search(word):
                            return word


def runGame(trie, graph):

    sleep(2)

    while True:
        im = grabImage()
        foundText = image_to_string(im)
        #print(foundText)

        # Start of the game, just hit enter
        if "Start" in foundText:
            press("enter")

        # When a fight is about to start
        elif "Start the Fight" in foundText:
            press("enter")

        # A gameboard has been found, run wordsearch
        elif "Shuffle" in foundText:
            status = wordSearch(trie, graph)

            if status == "None found":

                print(status + ", shuffling")
                keyDown("shift")
                keyUp("shift")
                sleep(3)

            elif status == "Words found":
                print("Typing...\n")

                for word in graph.words:
                    typewrite(word.lower(), interval=0.1)
                    press("enter")

                sleep(1)

        # End of a battle, hit enter
        elif "Gold Earned" in foundText:
            press("enter")

        # Heroes have found a shrine
        elif "ncient Shrin" in foundText:
            i = random.randint(0, 3)
            gods = ["s", "a", "w", "l"]
            typewrite(gods[i])
            sleep(1)
            press("enter")

        # Loot Chest has been found
        elif "Loot Chest" in foundText:
            press("enter")

            print("Enter the two 5 letter combinations:")
            i1 = input("Enter first value: ")
            i2 = input("Enter second value: ")

            key = treasure(trie, [i1, i2])
            sleep(2)  # To give you a chance to click back on game

            if key != None:
                typewrite(key.lower(), interval=0.1)
                press("enter")

            else:
                print("Word not found")


            sleep(5)

        # Devious Trap has been found
        # TODO Think of an algorithm to get rid of all words
        elif "Ready\n\na Ka" in foundText:
            print("Trap not yet implemented, try to do it yourself in 60 seconds")
            sleep(60)

        # Potion Shop, bot doesn't need help!
        elif "The Potion Shop" in foundText:
            typewrite("p")

        # Found a fountain, will give 20 seconds to upgrade heroes
        elif "The Fountain" in foundText:
            typewrite("g")
            print("You have 20 seconds to upgrade your heroes")
            sleep(10)
            print("10 seconds remain")
            sleep(5)
            print("5 left, finish up")
            typewrite("f")

        # Blacksmith, will give 30 seconds to buy things
        elif "The Blacksmith" in foundText:
            typewrite("b")
            print("You have 30 seconds to upgrade your heroes\nin the shop")
            sleep(25)
            print("5 seconds remain, finish up!")

        # Medicine man, poor dude can't make a living
        elif "edicin" in foundText:
            typewrite("o")

        elif "Book" in foundText:
            typewrite("r")
            sleep(5)
            typewrite("c")
            sleep(1)
            typewrite("l")





