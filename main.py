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
from storage import load_notes, save_notes
import json
import os


def main():
    notes = load_notes()
    while True:
        print("1. Add a note \n2. Show all notes \n3. Delete a note \n4. Exit")
        user_input = input("Enter a number: ")
        if user_input != "4":
            if user_input == "1":
                notes.append(
                    add_note(
                        5, "finish the project", "20-3-2025", "finish it in 3 days"
                    )
                )
                save_notes(notes)
            elif user_input == "2":
                for note in notes:
                    # print(note)
                    print("----------")
                    print(
                        f"Title: {note["title"]}\nId: {note["id"]}\nContent: {note["content"]}\nDate: {note["date"]}",
                    )
                    # TODO Add colorama
                    print("----------")
            continue
        else:
            sys.exit()


if __name__ == "__main__":
    main()
