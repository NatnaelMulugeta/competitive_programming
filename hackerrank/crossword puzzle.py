import math
import os
import random
import re
import sys

def get_space(crossword, word):
    for r in range(10):
        for c in range(10 - len(word) + 1):
            good = True
            for w in range(len(word)):
                if crossword[r][c + w] not in ['-', word[w]]:
                    good = False
                    break
            if good:
                yield (r, c, 0)
    
    for r in range(10 - len(word) + 1):
        for c in range(10):
            good = True
            for w in range(len(word)):
                if crossword[r + w][c] not in ['-', word[w]]:
                    good = False
                    break
            if good:
                yield (r, c, 1)

def write(crossword, word, spot):
    r, c, polar = spot
    if polar == 0:
        for w in range(len(word)):
            crossword[r][c + w] = word[w]
    else:
        for w in range(len(word)):
            crossword[r + w][c] = word[w]
            
def ctl_z(crossword, word, spot):
    r, c, polar = spot
    if polar == 0:
        for w in range(len(word)):
            crossword[r][c + w] = '-'
    else:
        for w in range(len(word)):
            crossword[r + w][c] = '-'
            
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

    
# if __name__ == "__main__":
#     crossword = []
#     for _ in range(10):
#         crossword.append(list(input()))
#     words = str(input()).split(";")
    
#     crosswordPuzzle(crossword, words)

