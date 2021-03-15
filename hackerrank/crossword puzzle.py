import math
import os
import random
import re
import sys

def get_space(crossword, word):
    for i in range(10):
        for j in range(10 - len(word) + 1):
            good = True
            for k in range(len(word)):
                if crossword[i][j + k] not in ['-', word[k]]:
                    good = False
                    break
            if good:
                yield (i, j, 0)
    
    for i in range(10 - len(word) + 1):
        for j in range(10):
            good = True
            for k in range(len(word)):
                if crossword[i + k][j] not in ['-', word[k]]:
                    good = False
                    break
            if good:
                yield (i, j, 1)

def write(crossword, word, spot):
    i, j, polar = spot
    if polar == 0:
        for k in range(len(word)):
            crossword[i][j + k] = word[k]
    else:
        for k in range(len(word)):
            crossword[i + k][j] = word[k]
            
def ctl_z(crossword, word, spot):
    i, j, polar = spot
    if polar == 0:
        for k in range(len(word)):
            crossword[i][j + k] = '-'
    else:
        for k in range(len(word)):
            crossword[i + k][j] = '-'
            
def crosswordPuzzle(crossword, words):
    if len(words) == 0:
        for row in crossword:
            print(''.join(row))
                
        return

    word = words.pop()

    available_spots = []
    for spot in get_space(crossword, word):
        available_spots.append(spot)

    for spot in available_spots:
        write(crossword, word, spot)
        crosswordPuzzle(crossword, words)
        ctl_z(crossword, word, spot)

    words.append(word)

    
if __name__ == "__main__":
    crossword = []
    for _ in range(10):
        crossword.append(list(input()))
    words = str(input()).split(";")
    
    crosswordPuzzle(crossword, words)

