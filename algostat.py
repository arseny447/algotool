import webbrowser
from urllib.parse import urlparse, parse_qs

def main():
    # тута просим ссылку
    url = input("Введите URL проекта: ").strip()
    
    # тута берём цифры
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    # тута проверка
    project_id = query_params.get('projectId')
    if not project_id:
        print("Ошибка: projectId не найден в URL")
        return
    
    # тута делаем ссылку
    new_url = f"https://learn.algoritmika.org/api/v1/projects/info/{project_id[0]}"
    print("Открываю:", new_url)
    
    # тута открываем
    webbrowser.open(new_url)

if __name__ == "__main__":
    main()
