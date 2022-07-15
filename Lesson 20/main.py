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