import os
import json
import datetime


def get_file_name_for(note_id):
    """ Возвращает имя файла для заметки с указанным ID """
    return f"notes/{note_id}.json"


def note_exists(note_id):
    """ Определяет, существует ли заметка с указанным ID """
    return os.path.exists(get_file_name_for(note_id))


def save_note(note):
    """ Сохраняет переданную заметку в файл """
    filename = get_file_name_for(note['id'])
    with open(filename, 'w') as f:
        json.dump(note, f)


def create_note(note_id, title, body):
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created": str(datetime.datetime.now()),
        "updated": None
    }
    return note


def edit_note(note_id, new_title, new_body):
    filename = get_file_name_for(note_id)
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            note = json.load(f)
        note['title'] = new_title
        note['body'] = new_body
        note['updated'] = str(datetime.datetime.now())
        save_note(note)
    else:
        print("WARNING: Note not found.")
    

def delete_note(note_id):
    filename = get_file_name_for(note_id)
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("WARNING: Note not found.")


def read_notes():
    notes = []
    for file in os.listdir("notes"):
        with open(os.path.join("notes", file), 'r') as f:
            note = json.load(f)
            notes.append(note)
    return notes


def main():
    while True:
        print("\nMenu:")
        print("[1]-Create   [2]-Read all notes   [3]-Edit   [4]-Delete   [5]-Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            note_id = input("Enter note ID: ")
            # check note already exists
            if note_exists(note_id):
                print("WARNING: Note with such ID already exists! Use 'Edit' operation.")
                continue
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            note = create_note(note_id, title, body)
            save_note(note)
            print("Note saved successfully.")

        elif choice == "2":
            print("All notes:")
            print("----------------------------------------------------------------------------------------------------")
            notes = read_notes()
            for note in notes:
                print(f"#{note['id']}: {note['title']} :::: {note['body']}, (created/updated : {note['created']}/{note['updated']})")
            print("----------------------------------------------------------------------------------------------------")    

        elif choice == "3":
            note_id = input("Enter ID of note to edit: ")
            new_title = input("Enter new title: ")
            new_body = input("Enter new body: ")
            edit_note(note_id, new_title, new_body)
            print("Note edited successfully.")

        elif choice == "4":
            note_id = input("Enter ID of note to delete: ")
            delete_note(note_id)
            print("Note deleted successfully.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("WARNING: Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
