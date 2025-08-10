import webbrowser
from urllib.parse import urlparse, parse_qs
import sys
import time
import colorama
from colorama import Fore, Style

# Инициализация colorama для работы с цветами в Windows
colorama.init()

# Функция для вывода градиентного текста
def print_gradient(text, start_color=(0, 255, 0), end_color=(255, 0, 255)):
    """Выводит текст с градиентом от start_color к end_color"""
    # Конвертируем цвета из RGB в ANSI
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    # Создаем градиент
    length = len(text)
    gradient = []
    for i in range(length):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / length)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / length)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / length)
        gradient.append(f"{rgb_to_ansi(r, g, b)}{text[i]}")
    
    print(''.join(gradient) + Style.RESET_ALL)

# Главное меню
def main_menu():
    """Отображает главное меню с градиентом"""
    title = "✨ AlgoTool - Инструменты для Algoritmika ✨"
    options = [
        "1. Статистика о проектах",
        "2. Создать проект на Unity",
        "3. Создать видео-проект",
        "4. Взять проект с закрытыми ремиксами",
        "5. Алга в алге",
        "6. Поставить кастомную аву",
        "99. Выход"
    ]
    
    print_gradient(title)
    print("\n" + "-" * 50)
    for option in options:
        print_gradient(option)
    print("-" * 50)
    
    return input("\nВаш выбор: ")

# Основная логика программы
def main():
    while True:
        choice = main_menu()
        
        if choice == "1":
            print_gradient("\n🔍 Статистика о проекте")
            url = input("Введите URL проекта: ").strip()
            
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            project_id = query_params.get('projectId')
            
            if not project_id:
                print_gradient("❌ Ошибка: projectId не найден в URL", (255, 0, 0), (255, 0, 0))
            else:
                new_url = f"https://learn.algoritmika.org/api/v1/projects/info/{project_id[0]}"
                print_gradient(f"🌐 Открываю: {new_url}")
                webbrowser.open(new_url)
        
        elif choice == "2":
            print_gradient("\n🎮 Создание Unity проекта")
            webbrowser.open("https://learn.algoritmika.org/uploads/student/619666/unity/58183083/unity/2.html")
        
        elif choice == "3":
            print_gradient("\n🎥 Создание видео-проекта")
            webbrowser.open("https://learn.algoritmika.org/storage/project-previews/a7fa4541aa19c55ec78180d04541e3d9.svg?t=1753976010")
            webbrowser.open("https://learn.algoritmika.org/laboratory")
        
        elif choice == "4":
            print_gradient("\n🔒 Доступ к проекту с закрытыми ремиксами")
            tutorial = (
                "\nИнструкция:\n"
                "1. Используйте первую функцию для получения статистики проекта\n"
                "2. В разделе 'meta' найдите значения 'scratchid' или 'pythonid'\n"
                "3. В лаборатории создайте проект Python или Scratch\n"
                "4. В адресной строке редактора замените цифры ID на полученное значение\n"
            )
            print_gradient(tutorial)
        
        elif choice == "5":
            print_gradient("\n🧩 Алга в алге")
            print_gradient("Открываю сборник алгоритмов...")
            webbrowser.open("https://learn.algoritmika.org/uploads/student/70069026/unity/58330901/VseAlgoPacki/index.html")
        
        elif choice == "6":
            print_gradient("\n🖼️ Поставить кастомную аву")
            print_gradient("Открываю инструмент для установки аватара...")
            webbrowser.open("https://learn.algoritmika.org/uploads/student/368074/6897a56d11c3a.html")
        
        elif choice == "99":
            print_gradient("\n👋 До свидания!")
            time.sleep(1)
            sys.exit()
        
        else:
            print_gradient("\n❌ Неверный выбор. Пожалуйста, введите цифру из меню", (255, 0, 0), (255, 0, 0))
        
        # Пауза перед возвратом в меню
        input("\nНажмите Enter для возврата в меню...")
        print("\n" * 3)  # Несколько пустых строк для очистки

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_gradient("\n👋 Программа завершена по запросу пользователя")
        sys.exit(0)
