import webbrowser
from urllib.parse import urlparse, parse_qs

# Запрашиваем выбор пользователя
choice = input("Введите функцию:\n\n1. Статистика о проектах\n\n2. Создать проект на Unity\n\nВаш выбор: ")

if choice == "2":
    # Исправлено: добавлены кавычки вокруг URL
    webbrowser.open("https://learn.algoritmika.org/uploads/student/619666/unity/58183083/unity/2.html")

elif choice == "1":
    # Запрашиваем URL проекта
    url = input("Введите URL проекта: ").strip()
    
    # Извлекаем параметры из URL
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    # Проверяем наличие projectId
    project_id = query_params.get('projectId')
    if not project_id:
        print("Ошибка: projectId не найден в URL")
    else:
        # Формируем новый URL
        new_url = f"https://learn.algoritmika.org/api/v1/projects/info/{project_id[0]}"
        print("Открываю:", new_url)
        webbrowser.open(new_url)

else:
    print("Неверный выбор. Пожалуйста, введите 1 или 2.")
