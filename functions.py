import json
import os
import sys
from colorama import Fore, Back, Style
from art import *
from colorama import Fore
from tabulate import tabulate
from datetime import date
from fpdf import FPDF



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
    while True:
        id = int(input("See a note by it's id: "))
        try:
            note = notes[id - 1]
            table = [[note["title"], note["content"], note["id"], note["date"]]]
            print(tabulate(table, headers=["Title", "Content", "ID", "Created at"], tablefmt="fancy_grid"))
            break
        except IndexError:
            print("Please enter a valid number")
            continue


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
        print(Fore.MAGENTA + "All notes have been deleted. Please restart the program")
        print(Style.RESET_ALL)
        return []
    elif usr_permission == "n":
        return notes


def export_as_pdf(notes):
    class PDF(FPDF):
        def header(self):
            # Setting font: helvetica bold 15
            pdf.set_font('Times', size=24)
            # Moving cursor to the right:
            self.cell(80)
            # Printing title:
            self.cell(30, 10, "Focus Note",align="C")
            # Performing a line break:
            self.ln(20)

        def footer(self):
            # Position cursor at 1.5 cm from bottom:
            self.set_y(-15)
            # Setting font: helvetica italic 8
            self.set_font("helvetica", style="I", size=8)
            # Printing page number:
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=18)
    for note in notes:
        pdf.cell(0, 10, "----------", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 10, f"Title: {note['title']}", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 10, f"Content: {note["content"]}", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 10, f"Created At: {note["date"]}", new_x="LMARGIN", new_y="NEXT")

    pdf.output(f"notes_{str(date.today())}")
    print("Notes successfully exported as PDF.")
