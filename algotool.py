import webbrowser
from urllib.parse import urlparse, parse_qs

# Запрашиваем выбор пользователя
choice = input("Введите функцию:\n\n1. Статистика о проектах\n\n2 Создать проект на Unity\n\n3. Создать видео-проект\n\n4. Взять проект с закрытыми ремиксами Ваш выбор: ")

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

elif choice == "3":
    webbrowser.open("https://learn.algoritmika.org/storage/project-previews/a7fa4541aa19c55ec78180d04541e3d9.svg?t=1753976010")
    webbrowser.open("https://learn.algoritmika.org/laboratory")

elif choice == "4":
    import webbrowser
import requests
from urllib.parse import urlparse, parse_qs

def main():
    # Получаем projectId из URL
    url = input("URL проекта: ").strip()
    project_id = parse_qs(urlparse(url).query).get('projectId', [None])[0]
    if not project_id: return print("Ошибка: projectId не найден")

    # Получаем метаданные и ищем нужный ID
    try:
        data = requests.get(f"https://learn.algoritmika.org/api/v1/projects/info/{project_id}").json()
        editor = next((k for k in ['scratchid', 'pythonid'] if k in data), None)
        if editor: webbrowser.open(f"https://learn.algoritmika.org/{editor[:-2]}/editor?project={data[editor]}")
    except: print("Ошибка при обработке проекта")
    
if __name__ == "__main__": main()

else:
    print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")

