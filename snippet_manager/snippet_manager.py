"""
A Python module that allows users to manage and store code snippets for easy retrieval. 
This module will support basic CRUD (Create, Read, Update, Delete) operations, 
enabling users to add, view, edit, and delete code snippets as needed. 
"""

import json
import tabulate


def check(title, code):
    """Helper function to check inputs"""
    assert len(title) != 0, "Title cant be empty!!"
    assert len(code) != 0, "Code cant be empty!!"


def add_snippet(title, description, code):
    """Adds a new code snippet with a specified title, description, and code content."""
    check(title, code)
    snippet = {"title": title, "description": description, "code": code}

    with open("snippets.json", "r+") as jsonfile:
        snippets = json.load(jsonfile)
        if len(snippets) == 0:
            snippet["id"] = 1
        else:
            last_id = snippets[-1]["id"]
            snippet["id"] = last_id + 1
        snippets.append(snippet)
        jsonfile.seek(0)
        json.dump(snippets, jsonfile, indent=4)
        jsonfile.truncate()


def list_snippets():
    """Allows users to list and view all currently stored code snippets."""
    headers = ["ID", "Title", "Description", "Code"]
    with open("snippets.json", "r") as jsonfile:
        snippets = json.load(jsonfile)
        if len(snippets) == 0:
            print("No snippets found.")
        else:
            data = [[s["id"], s["title"], s["description"], s["code"]]
                    for s in snippets]
            print(tabulate.tabulate(data, headers=headers))


def edit_snippet(ID, new_title, new_description, new_code):
    """Provide the ability to modify the title, description, or code content of an existing code snippet."""
    check(new_title, new_code)
    snippet = {"id": ID, "title": new_title,
               "description": new_description, "code": new_code}

    with open("snippets.json", "r+") as jsonfile:
        snippets = json.load(jsonfile)
        index = ID-1
        assert 0 <= index < len(snippets), "Invalid id!!"
        snippets[index] = snippet
        jsonfile.seek(0)
        json.dump(snippets, jsonfile, indent=4)
        jsonfile.truncate()


def delete_snippet(ID):
    """Enable users to remove a specific code snippet based on its ID."""
    with open("snippets.json", "r+") as jsonfile:
        snippets = json.load(jsonfile)
        index = ID-1
        assert 0 <= index < len(snippets), "Invalid id!!"
        snippets.pop(index)
        jsonfile.seek(0)
        json.dump(snippets, jsonfile, indent=4)
        jsonfile.truncate()
