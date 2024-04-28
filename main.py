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