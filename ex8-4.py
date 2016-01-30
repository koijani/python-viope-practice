# -*- coding: cp1252 -*-

import time

FILE_NAME = "notebook.txt"

try:
    handle = open(FILE_NAME, "r")
    handle.close()
except Exception:
    print("No default notebook was found, created one.")


while True:

    print("Now using file "+ FILE_NAME +"\n(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit\n")
    choice = int(input("Please select one: "))

    if(choice == 1):
        try:
            handle = open(FILE_NAME, "r")
            content = handle.read()
            print(content)
            handle.close()
        except Exception:
            continue
    elif(choice == 2):
        handle = open(FILE_NAME, "a")
        note = input("Write a new note: ")
        curr_time = time.strftime("%X %x")
        handle.write(note +":::"+ curr_time + "\n")
        handle.close()
    elif(choice == 3):
        handle = open(FILE_NAME, "w")
        handle.close()
        print("Notes deleted.")
    elif(choice == 4):
        FILE_NAME = input("Give the name of the new file: ")

        try:
            handle = open(FILE_NAME, "r")
            handle.close()
        except Exception:
            print("No notebook with that name detected, created one.")

    elif(choice == 5):
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")