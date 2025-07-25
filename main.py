import sys
from functions import (
    greeting,
    add_note,
    view_all_notes,
    view_one_note,
    edit_note,
    delete_notes,
    exit_prog,
    go_to_menu,
    export_as_pdf
)
from colorama import Fore, Back, Style
from storage import load_notes, save_notes
import json
import os
from art import *


def main():
    try:
        greeting()
        notes = load_notes()
        while True:
            print(
                "\n1. Add a note \n2. View all notes \n3. View one note \n4. Edit a note \n5. Delete all notes \n6. Export notes as PDF\n7. Exit"
            )
            user_input = input("Enter a number: ")
            if user_input == "1":
                notes.append(add_note(len(notes)))
                save_notes(notes)
                print("Your note has been saved!")
                go_to_menu()

            elif user_input == "2":
                view_all_notes(notes)
                go_to_menu()
            elif user_input == "3":
                view_one_note(notes)
                go_to_menu()
            elif user_input == "4":
                id, note = edit_note(notes)
                notes[id - 1] = note
                save_notes(notes)
                go_to_menu()
            elif user_input == "5":
                save_notes(delete_notes(notes))
                go_to_menu()
            elif user_input == "6":
                export_as_pdf(notes)
                go_to_menu()
            elif user_input == "7":
                exit_prog()
            print("\nPlease enter a valid choice\n")
            continue
    except KeyboardInterrupt:   
        exit_prog()
    
if __name__ == "__main__":
    main()
