import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}  # {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo['userId']] += 1  # {1: 2}
        except KeyError:
            todos_by_user[todo['userId']] = 1  # {1: 1, 2: 1, 3: 1}
print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]

max_complete = top_users[0][1]
print(max_complete)  # 12

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:  # 11 < 12
        break
    users.append(str(user))
print(users)  # ['5', '10']

max_users = " and ".join(users)
print(max_users)
print(f"Users {max_users} completed {max_complete} Todos")

max_todos = []  # создаем пустой список, куда будут попадать нужные todo
for todo in todos:
    if todo["completed"] and str(todo["userId"]) in users:
        # проходим по всем словарям в цикле с заданными условиями и добавляем нужный в список
        max_todos.append(todo)

with open("max_todos.json", "w") as f:  # записываем полученный список словарей todo в файл json
    json.dump(max_todos, f, indent=2)
