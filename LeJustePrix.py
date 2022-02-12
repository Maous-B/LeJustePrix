#!usr/bin/env python3
import random

prix = random.randint(1,1000)
#print(prix)
entreeclavier = int(input("Entrez le prix : "))
while prix != entreeclavier:
    if prix<entreeclavier:
        entreeclavier = int(input("Le prix que vous avez entrer est élevé, réessayez et entrez le prix : "))
    elif prix>entreeclavier:
        entreeclavier = int(input("Le prix que vous avez entrer est faible, réessayez et entrez le prix : "))
    elif prix == entreeclavier:
        str(print("Bravo, vous avez deviner le prix qui était de " + str(entreeclavier) + "€"))
        exit()