import numpy as np
import matplotlib.pyplot as plt
with open("words.txt", "r") as f:
    __words = f.readlines()
    words = []
    for i in range(len(__words)):
        words.append(__words[i].strip('\n'))

WORD_TO_ANALYSE = "weary"
NUMBER_OF_RUNS = 1


def ask_user():
    _input = input("Input a 5 letter word")
    if len(_input) != 5:
        raise Exception("Length of word given does not equal 5")
    else:
        return _input


def checker(word, guess):
    Exact_Match = []
    Yellow_Match = []
    listed_word = list(word)
    listed_guess = list(guess)
    for g_id, g_letter in enumerate(listed_guess):
        for l_id, l_letter in enumerate(listed_word):
            if g_letter == l_letter and g_id == l_id:
                Exact_Match.append(g_id)
                if g_id in Yellow_Match:
                    Yellow_Match.remove(g_id)
            elif g_letter == l_letter and g_id != l_id:
                if g_id not in Yellow_Match and g_id not in Exact_Match:
                    Yellow_Match.append(g_id)
    return Exact_Match, Yellow_Match


def game(user_guess, words_p):
    POSSIBLE_WORDS = []
    choice = np.random.choice(words_p)
    NOT_CHAR = []
    MUST_CHAR = []
    INDEX_CHAR = []
    ALL_OUTCOMES = []
    print(choice)
    Exact_Match, Yellow_Match = checker(choice, user_guess)
    for n in range(5):
        if n not in Exact_Match and n not in Yellow_Match:
            NOT_CHAR.append(user_guess[n])
    for i in Exact_Match:
        INDEX_CHAR.append((user_guess[i], i))
        MUST_CHAR.append(user_guess[i])
    for i in Yellow_Match:
        MUST_CHAR.append(user_guess[i])
    print(f"NOT = {NOT_CHAR} // MUST = {MUST_CHAR} // INDEX = {INDEX_CHAR} ")
    print(user_guess)
    for word in words:
        possible_outcome = 0
        print(f"Analysing Word: {word}")
        _word = list(word)
        Follow = True
        Index_check = True
        for INDEX_word in INDEX_CHAR:
            if INDEX_word in _word:
                if INDEX_CHAR.index(INDEX_word) == _word.index(INDEX_word):
                    print("INDEX")
                    Index_check = False
                    POSSIBLE_WORDS.append(INDEX_word)
                    possible_outcome = 1
            elif Index_check:
                Follow = False
        if Follow:
            for MUST_word in MUST_CHAR:
                if MUST_word in _word and MUST_CHAR.index(MUST_word) != _word.index(MUST_word):
                    print("MUST")
                    POSSIBLE_WORDS.append(MUST_word)
                    possible_outcome = 1
        if Follow:
            for NOT_word in NOT_CHAR:
                if NOT_word in _word:
                    print("NOT")
                    POSSIBLE_WORDS.append(NOT_word)
                    possible_outcome = 0
                else:
                    possible_outcome = 1
        if possible_outcome == 1:
            ALL_OUTCOMES.append(word)
    print(len(ALL_OUTCOMES))
    print(len(words))
    print(f"Possible Outcomes {(len(ALL_OUTCOMES)/len(words))*100}")


if __name__ == '__main__':
    game(WORD_TO_ANALYSE, words_p=words)
