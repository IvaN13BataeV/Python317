from bs4 import BeautifulSoup
import requests
import csv


class Parser:
    html = ""
    data = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="topnews__column")
        for item in news:
            header = item.find("h3").text
            href = item.find('a').get('href')
            time = item.find('time').text
            self.data.append({
                "Заголовок": header,
                "Ссылка": href,
                "Время": time
                })

    def save(self):
        with open(self.path, "w") as f:
            writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=self.data[0].keys())
            writer.writeheader()
            for d in self.data:
                writer.writerow(d)
        print("Сохранение данных в файл прошло успешно")
        print("Сохранены следующие новости:", self.data)

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
