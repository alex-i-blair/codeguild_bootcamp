# from graphics.py import *

import random
import os
import sys

def get_word():
    x = random.randint(1,100000)
    count = 0
    with open("word_list.txt") as word_list:
        for word in word_list:
            if count == x:
                break
            else:
                count += 1
    return list(word.strip())

def display_word(word):
    user_guess = list("_" * len(word))
    for ch in user_guess:
        print ch,

def game():
    word_to_guess = get_word()
    print """Welcome to Hangman+++!"
    I've selected a word for you that is %d letters long.""" % len(word_to_guess)
    print display_word(word_to_guess)
    incorrect_guesses = []
    current_state = list("_" * len(word_to_guess))
    # print word_to_guess
    guesses = 0
    while guesses <=6:
        # print word_to_guess
        ch = raw_input("Guess a letter, ya dingus!:  ")
        match_list = find_matches(word_to_guess,ch)
        if len(match_list) == 0:
            guesses += 1
            incorrect_guesses.append(ch)
        # for a_letter in current_state and incorrect_guesses:
        #     if a_letter == ch:
        #         print "You already guessed that letter, ya dingas!"

        else:
            for matching_index in match_list:
                current_state[matching_index] = word_to_guess[matching_index]

            if current_state == word_to_guess:
                os.system("clear")
                print ''.join(word_to_guess).title()
                print "Nice work dingas! You didn't lose!"
                return
        os.system('clear')
        print ' '.join(current_state)
        print ', '.join(incorrect_guesses)

    print "Tough shit, loser!"
    print "The word was:  ", ''.join(word_to_guess).title()
def find_matches(word_to_guess, ch):
    result = []
    for index,letter in enumerate(word_to_guess):
        if letter == ch:
            result.append(index)
    return result

game()