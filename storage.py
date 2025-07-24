import os 
import json
def load_notes():
    with open("notes.json") as f:
        notes_list = json.load(f)
        return notes_list
def save_notes(note_list):
    with open("notes.json", "w") as f:
        json.dump(note_list, f)

