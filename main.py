import sys
from functions import (
    add_note,
    view_all_notes,
    view_one_note,
    edit_note,
    delete_note,
    exit_prog,
    notes_len,
)
from colorama import Fore, Back, Style
from storage import load_notes, save_notes
import json
import os


def main():
    print(Fore.RED + "Welcome To FocusNote")
    print(Style.RESET_ALL)
    notes = load_notes()
    while True:
        print(
            "1. Add a note \n2. View all notes \n3. View one note \n4. Edit a note \n5. Delete a note \n6. Exit"
        )
        user_input = input("Enter a number: ")
        if user_input != "6":
            if user_input == "1":
                notes.append(add_note(len(notes)))
                save_notes(notes)
                print("Your note has been saved!")
            elif user_input == "2":
                # print(note)
                view_all_notes(notes)
            elif user_input == "3":
                view_one_note(notes)
            continue
        else:
            sys.exit()


if __name__ == "__main__":
    main()
