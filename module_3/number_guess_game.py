# -*- coding: utf-8 -*-
"""number_guess_game.ipynb

Sayı Tahmin Oyunu: İleri seviye (min-max ipucu, puan sistemi ile)     
Number Guess Game: Advanced Level (with minimum and maximum hints and a scoring system)
"""

import random

gizli = random.randint(1, 100)
puan = 100
alt, ust = 1, 100

print("Sayı Tahmin Oyunu (1-100)\n")

while True:
    print(f"Aralık: {alt} - {ust}")
    tahmin = int(input("Tahmin: "))

    if tahmin == gizli:
        print(f"Tebrikler! Doğru bildin. Puanın: {puan}")
        break

    puan -= 10

    if tahmin < gizli:
        print("Daha büyük!")
        alt = tahmin + 1
    else:
        print("Daha küçük!")
        ust = tahmin - 1

    if puan <= 0:
        print(f"Kaybettin! Doğru sayı: {gizli}")
        break

"""**fonksiyon ile yaparsak**"""

import random

def number_guess_game():
    secret = random.randint(1, 100)
    score = 100
    low, high = 1, 100

    print("Number Guessing Game (1–100)\n")

    while True:
        print(f"Range: {low} - {high}")
        guess = int(input("Your guess: "))

        if guess == secret:
            print(f"Congratulations! You guessed it. Your score: {score}")
            break

        score -= 10

        if guess < secret:
            print("Higher!")
            low = guess + 1
        else:
            print("Lower!")
            high = guess - 1

        if score <= 0:
            print(f"You lost! The correct number was: {secret}")
            break


# START THE GAME
number_guess_game()
