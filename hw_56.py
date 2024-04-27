from hw_parser import Parser


def main():
    pars = Parser("https://lenta.ru/", "news.csv")
    pars.run()


if __name__ == '__main__':
    main()
