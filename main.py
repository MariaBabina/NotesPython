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