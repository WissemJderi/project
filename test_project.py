import pytest
from datetime import date
from functions import add_note, delete_notes, view_all_notes

def test_add_note(monkeypatch):
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "Test Title" if _.startswith("Enter a title") else "Test Content")
    result = add_note(0)
    assert result["id"] == 1
    assert result["title"] == "Test Title"
    assert result["content"] == "Test Content"
    assert result["date"] == str(date.today())

def test_delete_notes_yes(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    notes = [{"id": 1, "title": "A", "content": "B", "date": "2025-07-25"}]
    result = delete_notes(notes)
    assert result == []

def test_delete_notes_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "n")
    notes = [{"id": 1, "title": "A", "content": "B", "date": "2025-07-25"}]
    result = delete_notes(notes)
    assert result == notes

def test_view_all_notes(capsys):
    notes = [{"id": 1, "title": "A", "content": "B", "date": "2025-07-25"}]
    view_all_notes(notes)
    captured = capsys.readouterr()
    assert "Notes created: 1" in captured.out
    assert "A" in captured.out
    assert "B" in captured.out

