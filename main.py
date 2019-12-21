from trie import Trie
from gameLogic import wordSearch, treasure, runGame
from gameboardGraph import gameboardGraph
from pynput.keyboard import Key, Controller
import random
import numpy as np





def buildTrie():
    t = Trie()
    with open("words.txt", "r") as f:

        for word in f.readlines():
            t.insert(word[:-1])

    return t


def convertwords():

    new = open("words.txt", "w+")

    with open("usa2.txt", "r") as f:
        for line in f.readlines():
            cap = line.upper()
            if cap[:-1].isalpha() and len(cap) > 4 and len(cap) < 9:
                new.write(cap)


def main():

    t = buildTrie()

    g = gameboardGraph()

    runGame(t, g)



    ''' This is in case of a character death
    while True:
        wordShuff = ["R", "G", "T", "O", "I", "L", "Y"]
        random.shuffle(wordShuff)
        word = ''.join(wordShuff[:7])
        if trie.search(word):
            print(word)'''



if __name__ == "__main__":
    main()
