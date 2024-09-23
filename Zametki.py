import json
import os
from datetime import datetime

# Имя файла, в который будут сохраняться заметки
NOTES_FILE = 'notes.json'

# Функция для загрузки заметок из файла
def load_notes():
    pass

# Функция для сохранения заметок в файл
def save_notes(notes):
    pass

# Функция для добавления заметки
def add_note():
    pass

# Функция для просмотра всех заметок
def view_notes():
    pass

# Функция для изменения заметки
def edit_note():
    pass

# Функция для удаления заметки
def delete_note():
    pass

# Функция для сортировки заметок по времени
def sort_notes():
    pass

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