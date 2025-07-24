import json
import os

from colorama import Fore, Back, Style
from art import *
from colorama import Fore

def greeting(): 
    app_title = "Focus Note" 
    print(Fore.RED + text2art(app_title, "big" ))
    print(Style.RESET_ALL)

def add_note(notes_len):
    title = input("Enter a title: ")
    content = input("Enter note content: ")
    id = notes_len + 1
    time_created = "20-02-2025"

    return {"id": id, "title": title, "date": time_created, "content": content}


def view_all_notes(notes):
    print(f"Notes created: {len(notes)} ")
    for note in notes:
        
        print("----------")
        print(
            f"Title: {note["title"]}\nId: {note["id"]}\nContent: {note["content"]}\nDate: {note["date"]}"
        )
        # TODO Add colorama
        print("----------")


def view_one_note(notes):
    id = int(input("See a note by it's id"))
    print(notes[id + 1])


def edit_note():
    print("Working From edit_note")


def delete_note():
    print("Working From delete_note")


def exit_prog():
    print("Working From exit_prog")


def notes_len():
    print("Working From notes_len")
