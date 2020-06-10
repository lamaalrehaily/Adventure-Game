import time
import random
import sys


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


names_set = {'Monsters', 'Ants', 'Cockroaches'}
name = random.choice(tuple(names_set))


def intro():
    print_pause("You wake up and find yourself in a dark room,")
    print_pause("You look for the light switch,")
    print_pause("But you don't find it,")
    time.sleep(1)
    print(name, "wearing white neon clothes covering all their",
                "body approaches to you,")
    print_pause("You ask for his name but he doesn't answer,")
    time.sleep(1)
    print("He only tells you to follow him and enter room number",
          "one,")
    time.sleep(1)
    print("You follow him and he suddenly disappears but two",
          "doors appear in front of you.")


def room_one(items):
    print_pause("You open the door")
    print_pause("You find yourself in line waiting")
    if "kingdom_sword" in items:
        time.sleep(1)
        print("You have already collected the kingdom sword there is",
              "nothing more",
              "to do here, you should head back to the dark room")
    else:
        time.sleep(1)
        print("Cute little", name, "greet you and give you the kingdom",
              "sword")
        items.append("kingdom_sword")
    print_pause("You head back to the dark room")
    horror_rooms(items)


def room_two(items):
    print_pause("You enter the room quietly and start walking,")
    time.sleep(1)
    print("after a few you moments you start hearing some echo,",
          "buzzing!! OMG!!")
    time.sleep(1)
    print("IT IS FLYING", name, "!")
    if "exit_key" in items:
        time.sleep(1)
        print("You have already defeated the", name, "there is nothing",
              "more to do here, goodbye!")
    else:
        time.sleep(1)
        print("The flying", name, "start attacking you!")
        if "kingdom_sword" in items:
            time.sleep(1)
            print("So you take out the kingdom sword you collected",
                  "in room 1")
            time.sleep(1)
            print("Sudden talking fire comes out of it to help you",
                  "defeat the", name, "!")
            time.sleep(1)
            print("Now you have defeated all the", name, "you are welcome",
                  "to close the game.")
            print_pause("You win!")
            print_pause("Goodbye!")
            items.append("exit_key")
            while True:
                again = str(input("Do you want to play again (type yes "
                                  "or no): "))
                if again.upper() == "YES":
                    play_game()
                elif again.upper() == "NO":
                    sys.exit(0)
                else:
                    print("Sorry, I don't understand")
        else:
            time.sleep(1)
            print("The", name, "hit you with a shotgun")
            time.sleep(1)
            print("You bleed to death...unfortunatly you have been",
                  "defeated.")
            print_pause("You lost")
            print_pause("Game Over!")
            print_pause("Would you like to play again?")
            while True:
                again = str(input("Do you want to play again (type yes "
                                  "or no): "))
                if again.upper() == "YES":
                    play_game()
                elif again.upper() == "NO":
                    sys.exit(0)
                else:
                    print("Sorry, I don't understand")
    print_pause("You head back to the dark room.")
    horror_rooms(items)


def horror_rooms(items):
    while True:
        print_pause("Which of these rooms would you like to enter?")
        room = input("1. Room 1\n"
                     "2. Room 2\n")
        if room == '1':
            room_one(items)
        elif room == '2':
            room_two(items)
        else:
            print("Sorry, I don't understand")


def play_game():
    items = []
    intro()
    horror_rooms(items)


play_game()
