import json
from datetime import datetime
import datetime
import os

def read_notes():
    notes = []
    if os.path.exists('application_notes/notes.json'):
        try:
            with open('application_notes/notes.json', 'r', encoding='utf-8') as file:
                data = file.read()
                if data:
                    notes = [json.loads(note) for note in data.split(';') if note]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Ошибка при чтении заметок")
    return notes

def save_notes(notes):
    notes_str = ';'.join(json.dumps(note, ensure_ascii=False) for note in notes)
    with open('application_notes/notes.json', 'w', encoding='utf-8') as file:
        file.write(notes_str)

def add_note():
    try:
        title = input("Введите заголовок заметки: ")
        body = input("Введите содержание заметки: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes = read_notes()
        note_id = len(notes) + 1
        note = {
            "id": note_id,
            "title": title,
            "message": body,
            "timestamp": timestamp
        }
        notes.append(note)
        save_notes(notes)
        print("Заметка успешно сохранена")
    except Exception as err:
        print("Ошибка:", err)

def edit_note():
    show_notes()
    flag_exit = False
    while not flag_exit:
        answer = input("Введите id заметки для редактирования или exit для выхода: ")
        try:           
            notes = read_notes()
            if answer == 'exit':
                        print('Вот и правильно! Итак всё прекрасно было')
                        flag_exit = True
            elif answer != 'exit':
                note_id = int(answer)
                for note in notes:
                    if note["id"] == note_id:
                        title = input("Введите новый заголовок заметки: ")
                        body = input("Введите новое тело заметки: ")
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        note["title"] = title
                        note["message"] = body
                        note["timestamp"] = timestamp
                        save_notes(notes)
                        print("Заметка успешно отредактирована")
                        break
                else:
                    print("Заметка с указанным id не найдена")
        except ValueError:
            print("Ошибка: Некорректный формат запроса.")

def delete_note():
    try:
        notes = read_notes()
        delete_id = int(input("Введите id заметки для удаления: "))
        note_id = int(delete_id)
        for note in notes:
            if note["id"] == note_id:
                notes = [note for note in notes if note["id"] != delete_id]
                save_notes(notes)
                print("Заметка успешно удалена")
        else:
            print("Заметка с указанным id не найдена")
    except ValueError:
        print("Ошибка: Некорректный формат id заметки. Введите целое число.")

def filter_notes_by_date():
    try:
        date_str = input("Введите дату для фильтрации (ГГГГ-ММ-ДД): ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")
            return
        
        notes = read_notes()
        filtered_notes = [note for note in notes if note["timestamp"].startswith(date_str)]
        
        if filtered_notes:
            print("Результаты фильтрации: ")
            for note in filtered_notes:
                print(f"id: {note['id']}, Заголовок: {note['title']}, Содержание: {note['message']}, Дата/время: {note['timestamp']}")
        else:
            print("Нет заметок для указанной даты")
    except Exception as err:
        print("Ошибка:", err)

def show_notes():
    notes = read_notes()
    if notes:
        print("Список заметок:")
        for note in notes:
            print(f"id: {note['id']}, Заголовок: {note['title']}, Содержание: {note['message']}, Дата/время: {note['timestamp']}")
    else:
        print("Заметки отсутствуют")

def main():
    print('Давайте запишем вашу мысль')
    print()
    flag_exit = False
    while not flag_exit:
        command = input("Введите команду (add, edit, delete, filter, show, exit): ")
        if command == "add":
            add_note()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "filter":
            filter_notes_by_date()
        elif command == "show":
            show_notes()
        elif command == "exit":
            flag_exit = True
        else:
            print("Неверная команда. Попробуйте еще раз")

if __name__ == "__main__":
    main()