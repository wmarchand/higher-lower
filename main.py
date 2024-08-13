#My perfected code
from replit import clear
import random
from art import logo, vs
from game_data import data

def person():
    return random.choice(data)

def format_data(person):
    person_name = person["name"]
    person_descr = person["description"]
    person_country = person["country"]
    return f"{person_name}, a {person_descr}, from {person_country}"
    
def play(current_score, person_1, person_2):
    print(logo)
    if current_score != 0:
        print(f"You're right! Current score: {current_score}.")
    print(f"Compare A: {format_data(person_1)}")
    print(vs)
    print(f"Against B: {format_data(person_2)}")
    person_1_followers = person_1["follower_count"]
    person_2_followers = person_2["follower_count"]
    #Gameshark
    # print(f"person a = {person_1_followers}")
    # print(f"person b = {person_2_followers}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == "a" or choice == "1":
        if person_2_followers > person_1_followers:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
        elif person_1_followers > person_2_followers:
            clear()
            current_score += 1
            play(current_score, person_1, person())
        else:
            print(f"YOU GOT THE SAME PERSON!!! Your current score is {current_score}.")
            play(current_score, person_1, person())
    elif choice == "b" or choice == "2":
        if person_2_followers < person_1_followers:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
        elif person_1_followers < person_2_followers:
            clear()
            current_score += 1
            play(current_score, person_2, person())
        else:
            print(f"YOU GOT THE SAME PERSON!!! Your current score is {current_score}.")
            play(current_score, person_1, person())
    else:
        clear()
        print("I do not compute. Try again.")
        play(current_score, person_1, person_2)

current_score = 0
person_1 = person()
person_2 = person()
play(current_score, person_1, person_2)














#My original code
# from replit import clear
# import random
# from art import logo, vs
# from game_data import data

# def person():
#     return random.choice(data)
#     #who = random.choice(data)
#     # attributes = []
#     # for i in who:
#     #     attributes.append(who[i])
#     # return attributes

# def format_data(person):
#     person_name = person["name"]
#     person_descr = person["description"]
#     person_country = person["country"]
#     return f"{person_name}, a {person_descr}, from {person_country}"

# def convert_to_int(number):
#     return int(number)


# def play(current_score, person_1, person_2):
#     print(logo)
#     if current_score != 0:
#         print(f"You're right! Current score: {current_score}.")
#     # print(f"Compare A: {person_1[0]}, a {person_1[2]}, from {person_1[3]}")
#     # print(vs)
#     # print(f"Against B: {person_2[0]}, a {person_2[2]}, from {person_2[3]}")
#     print(f"Compare A: {format_data(person_1)}")
#     print(vs)
#     print(f"Against B: {format_data(person_2)}")
#     # person_1_followers = convert_to_int(person_1[1])
#     # person_2_followers = convert_to_int(person_2[1])
#     person_1_followers = person_1["follower_count"]
#     person_2_followers = person_2["follower_count"]
#     print(f"person a = {person_1_followers}")
#     print(f"person b = {person_2_followers}")
#     choice = input("Who has more followers? Type 'A' or 'B': ").lower()
#     if choice == "a" or choice == "1":
#         if person_2_followers > person_1_followers:
#             clear()
#             print(logo)
#             print(f"Sorry, that's wrong. Final score: {current_score}")
#         elif person_1_followers > person_2_followers:
#             clear()
#             current_score += 1
#             play(current_score, person_1, person())
#         else:
#             print(f"YOU GOT THE SAME PERSON!!! Your current score is {current_score}.")
#             play(current_score, person_1, person())
#     elif choice == "b" or choice == "2":
#         if person_2_followers < person_1_followers:
#             clear()
#             print(logo)
#             print(f"Sorry, that's wrong. Final score: {current_score}")
#         elif person_1_followers < person_2_followers:
#             clear()
#             current_score += 1
#             play(current_score, person_2, person())
#         else:
#             print(f"YOU GOT THE SAME PERSON!!! Your current score is {current_score}.")
#             play(current_score, person_1, person())
#     else:
#         clear()
#         print("I do not compute. Try again.")
#         play(current_score, person_1, person_2)

# current_score = 0
# person_1 = person()
# person_2 = person()
# play(current_score, person_1, person_2)
    




