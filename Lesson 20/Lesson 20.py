# Парсинг сайтов

"""
Парсинг сайтов

    Создаем новый проект


    Создаем файл requirements.txt и вносим туда данные:

        requests==2.27.1
        beautifulsoup4==4.11.1


    В командной строке пишем:

        pip install -r requirements.txt


    Заходим на сайт https://habr.com/ru/all/, нажимаем правой клавишей мыши по странице и просмотреть код. Переходим во вкладку
    Сеть - ищем файл с методом GET в котором будут статьи.


    Открываем файл main.py и пишем код:


        from datetime import datetime
        from pprint import pprint
        import requests
        from bs4 import BeautifulSoup


        def main():

            r = requests.get('https://habr.com/ru/all/')
            soup = BeautifulSoup(r.text, 'html.parser')
            article_tags = soup.find_all('article', class_='tm-articles-list__item')
            titles = []

            for article_tag in article_tags:
                title_tag = article_tag.find('h2')
                link_tag = title_tag.find('a')

                author_tag = article_tag.find('div', class_='tm-article-snippet__meta')

                if not link_tag:
                    continue

                titles.append((
                    link_tag.text,
                    link_tag['href'],
                    author_tag.find(class_='tm-user-info__username').text.strip(),
                    datetime.fromisoformat(author_tag.find('time')['datetime'][:-1]),
                ))

            pprint(titles)

        if __name__ == '__main__':
            main()

   * P.S. При запуске кода должна выдать <Response [200]> - значит все хорошо.
"""