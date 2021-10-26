from stars import list_of_stars
from os import system
import random



stars_list = []
star1 = random.choice(list_of_stars)
stars_list.append(star1)

def choose_new_star():
    new_star = random.choice(list_of_stars)
    while new_star == stars_list[0]:
        new_star = random.choice(list_of_stars)
    return new_star

star2 = choose_new_star()
stars_list.append(star2)

def update_list(stars_list):
    if stars_list[0]['followers']>stars_list[1]['followers']:
       stars_list[1] = choose_new_star()
       return stars_list
    else:   
        stars_list[0] = stars_list[1]
        stars_list[1] = choose_new_star()
        return stars_list





end_game = False
result = 0
while end_game is False:
    print(f"A: {stars_list[0]['name']} is a {stars_list[0]['description']} from {stars_list[0]['origin']}. ")
    print("\n VS \n")
    print(f"B: {stars_list[1]['name']} is a {stars_list[1]['description']} from {stars_list[1]['origin']}. ")

    user_guess = input("A or B ")

    if stars_list[0]['followers']>stars_list[1]['followers']:

        if user_guess == "a":
            print(f"That's right \n{stars_list[0]['name']} has {stars_list[0]['followers']} and  {stars_list[1]['name']} has {stars_list[1]['followers']} \n Current score is {result}")
            update_list(stars_list)
            result +=1
        else:
            print(f"Wrong\n{stars_list[0]['name']} has {stars_list[0]['followers']} and  {stars_list[1]['name']} has {stars_list[1]['followers']}")
            print(f"Your result is {result}")
            end_game = True
    else:
        if user_guess == "b":
            print(f"That's right \n{stars_list[1]['name']} has {stars_list[1]['followers']} and {stars_list[0]['name']} has {stars_list[0]['followers']} \n Current score is {result}")
            update_list(stars_list)
            result +=1
        else:
            print(f"Wrong\n{stars_list[1]['name']} has {stars_list[1]['followers']} and {stars_list[0]['name']} has {stars_list[0]['followers']}")
            print(f"Your result is {result}")
            end_game = True