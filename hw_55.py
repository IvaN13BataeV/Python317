import csv
import json
import requests

# записываем данные из json формата в список словарей
todos = json.loads(requests.get("https://jsonplaceholder.typicode.com/todos").text)

with open("todos.csv", 'w') as c:
    writer = csv.DictWriter(c, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
    writer.writeheader()
    for todo in todos:  # из текущего списка создаем csv файл с соответственным заполнением строк
        writer.writerow(todo)
