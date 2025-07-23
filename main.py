from functions import add_note, view_all_notes, view_one_note, edit_note,delete_note, exit_prog, notes_len
import json
import os


def main():
    """with open("notes.json", "a") as json_file: 
        note_dict = {
            "title": "learn python",
            "id": 1, 
            "date": "2025-07-23"
        }
        note_json = json.dumps(note_dict, indent=4)
        with open("notes.json", "a") as f: 
            f.write(note_json)"""
    add_note()
    # with open("notes.json", "r") as f : 
    #     json_obj = json.load(f)
    #
if __name__ == "__main__":
    main()
