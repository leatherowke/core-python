"""Restaurant rating lister."""


# put your code here
from pickle import APPEND
from turtle import ScrolledCanvas


def process_scores() :

    scores_txt = open("scores.txt")

    scores = {}

    for line in scores_txt :
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)
            
    return scores

def add_restaurant(scores) :
    print("add a restaurant and its rating!")
    restaurant = input("restaurant name:")
    rating = input("rating:")

    scores[restaurant] = rating

def print_sorted_scores(scores) :
    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")



scores = process_scores()
add_restaurant(scores)
print_sorted_scores(scores)