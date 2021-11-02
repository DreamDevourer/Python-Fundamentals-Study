#!/usr/bin/python3

import json
import sys
import os
import random

foodDict = {}
movieDict = {}

currentDir = os.path.dirname(sys.argv[0])


def randomFood():
    with open(f"{currentDir}/food.json", "r") as json_food:
        foodStored = json.load(json_food)
        foodDict = foodStored
        foodList = foodDict["foods"]
        randomFood = random.choice(foodList)
        return randomFood


def randomMovie():
    with open(f"{currentDir}/movies.json", "r") as json_movies:
        moviesStored = json.load(json_movies)
        movieDict = moviesStored
        movieList = movieDict["movies"]
        randomMovie = random.choice(movieList)
        return randomMovie


class main():
    userChoice = input("Would you like to eat or watch a movie? ")

    if userChoice == "eat" or userChoice == "food":
        print(randomFood())
    elif userChoice == "watch" or userChoice == "movie":
        print(randomMovie())
    else:
        print("Please enter eat or watch")
