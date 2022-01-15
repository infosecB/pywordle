import sys
from random import choice
from rich import print
from words import FIVE_LETTER_WORDS

words = FIVE_LETTER_WORDS
solved = False

def validate_english_word(word):
    if word in words:
        return True
    elif word[0:-1] in words:
        return True
    else:
        return False

def check_exact_match(answer, guess_letter, guess_index):
    if guess_index in [position for position, character in enumerate(answer) if character == guess_letter]:
        return True
    else:
        return False

def check_partial_match(answer, letter):
    if letter in list(answer):
        return True
    else:
        return False


answer = choice(words)

while not solved:
    print_result=""
    guess = input("\nType in your 5 letter guess (Q to quit): ")
    print("\n")
    if guess == 'Q':
        print("\nYou quit... The answer is: " + answer + "\n")
        break
    if len(guess)==5 and validate_english_word(guess):
        guess_index=0
        score=0
        for g in list(guess):
            if check_exact_match(answer, g, guess_index):
                print_result += "[green]" + g + "[/green]" + " "
                guess_index+=1
                score+=1
                if score==5:
                    solved=True
                    print("\nYou win! The answer is: [green]" + answer + "[/green]\n")
                    sys.exit()
                continue
            elif check_partial_match(answer, g):
                print_result += "[yellow]" + g + "[/yellow]" + " "
                guess_index+=1
                continue
            else:
                print_result += "[red]" + g + "[/red]" + " "
                guess_index+=1
        print(print_result)
    elif len(guess)!=5:
        print("Your guess is not 5 letters...")
    else:
        print("Your guess is not an english word...")