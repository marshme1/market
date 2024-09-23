import json
import os
from datetime import datetime

# Имя файла, в который будут сохраняться заметки
NOTES_FILE = 'notes.json'

# Функция для загрузки заметок из файла
def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as file:
        return json.load(file)

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для добавления заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    timestamp = datetime.now().isoformat()  # Получаем текущее время
    notes = load_notes()
    notes.append({
        'title': title,
        'content': content,
        'timestamp': timestamp
    })
    save_notes(notes)
    print("Заметка добавлена!")

# Функция для просмотра всех заметок
def view_notes():
    notes = load_notes()
    for index, note in enumerate(notes):
        print(f"{index + 1}. {note['title']} (создано: {note['timestamp']})")
        print(f"   {note['content']}n")

# Функция для изменения заметки
def edit_note():
    view_notes()
    note_index = int(input("Введите номер заметки для редактирования: ")) - 1
    notes = load_notes()
    if 0 <= note_index < len(notes):
        new_title = input("Введите новый заголовок: ")
        new_content = input("Введите новое содержание: ")
        notes[note_index]['title'] = new_title
        notes[note_index]['content'] = new_content
        save_notes(notes)
        print("Заметка изменена!")
    else:
        print("Неверный номер заметки.")

# Функция для удаления заметки
def delete_note():
    view_notes()
    note_index = int(input("Введите номер заметки для удаления: ")) - 1
    notes = load_notes()
    if 0 <= note_index < len(notes):
        notes.pop(note_index)
        save_notes(notes)
        print("Заметка удалена!")
    else:
        print("Неверный номер заметки.")

# Функция для сортировки заметок по времени
def sort_notes():
    notes = load_notes()
    notes.sort(key=lambda x: x['timestamp'])  # Сортируем по времени создания
    save_notes(notes)
    print("Заметки отсортированы по времени!")

# Главное меню
def main():
    while True:
        print("nМеню:")
        print("1. Добавить заметку")
        print("2. Посмотреть заметки")
        print("3. Изменить заметку")
        print("4. Удалить заметку")
        print("5. Отсортировать заметки по времени")
        print("6. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            sort_notes()
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()