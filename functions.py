import json
import os

def add_note():
    with open("notes.json", "r") as f:
        note_list= json.load(f)
    with open("notes.json", "w") as f:
        note_list.append({
        "id": 3,
        "title": "Review JSON",
        "date": "2025-07-23",
        "content": "Understand how to manipulate JSON in Python"
        })
        print(note_list)

def view_all_notes():
    print("Working From view_all_notes")

def view_one_note():
    print("Working From view_one_note")

def edit_note():
    print("Working From edit_note")

def delete_note():
    print("Working From delete_note")

def exit_prog():
    print("Working From exit_prog")

def notes_len():
    print("Working From notes_len")
