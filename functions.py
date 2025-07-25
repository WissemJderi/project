import json
import os
import sys
from colorama import Fore, Back, Style
from art import *
from colorama import Fore
from tabulate import tabulate
from datetime import date
def go_to_menu():
    while True:
        user_input = input("Hit Enter to return to the menu. ")
        if user_input.strip() == "":
            return True
        continue


def greeting():
    app_title = "Focus Note"
    print(Fore.RED + text2art(app_title, "big"))
    print(Style.RESET_ALL)


def add_note(notes_len):
    title = input("Enter a title: ")
    content = input("Enter note content: ")
    id = notes_len + 1
    time_created = str(date.today())

    return {"id": id, "title": title, "date": time_created, "content": content}


def view_all_notes(notes):
    if len(notes) == 0:
        print("\nNo notes found. Go to the menu to add one.\n")
        return
    print(f"\nNotes created: {len(notes)} ")
    table = []
    for note in notes:
        table.append([note["title"], note["content"], note["id"], note["date"]])
    print(tabulate(table, headers=["Title", "Content", "ID", "Created at"], tablefmt="fancy_grid"))


def view_one_note(notes):
    id = int(input("See a note by it's id: "))
    note = notes[id - 1]
    table = [[note["title"], note["content"], note["id"], note["date"]]]
    print(tabulate(table, headers=["Title", "Content", "ID", "Created at"], tablefmt="fancy_grid"))


def edit_note(notes):
    note_id = int(input("Please enter the note id: "))
    note = notes[note_id - 1]
    table = [[note["title"], note["content"], note["id"], note["date"]]]
    print(tabulate(table, headers=["Title", "Content", "ID", "Created at"], tablefmt="fancy_grid"))


    while True:
        update_note_by = input("Update note? (t = title, c = content): ")
        if update_note_by == "t":
            new_data = input("Start typing: ").strip()
            note["title"] = new_data
            print(Fore.MAGENTA + "Note successfully edited.")
            print(Style.RESET_ALL)
            return note_id, note
        elif update_note_by == "c":
            new_data = input("Start typing: ").strip()
            note["content"] = new_data
            print(Fore.MAGENTA + "Note successfully edited.")
            print(Style.RESET_ALL)
            return note_id, note
        else:
            continue


def delete_notes(notes):
    usr_permission = input("Are you sure? (y = yes, n = no) ")
    if usr_permission == "y":
        print(Fore.MAGENTA + "All notes have been deleted.")
        print(Style.RESET_ALL)
        return []
    elif usr_permission == "n":
        return notes


def exit_prog():
    print("\n")
    sys.exit()

def notes_len():
    print("Working From notes_len")
