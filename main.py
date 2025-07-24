from functions import add_note, view_all_notes, view_one_note, edit_note,delete_note, exit_prog, notes_len
from storage import load_notes, save_notes
import json
import os

def main():
    notes =  load_notes()
    notes.append(add_note("finish the project", 5, "20-3-2025", "finish it in 3 days"))
    save_notes(notes)



if __name__ == "__main__":
    main()
