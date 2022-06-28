from tech_news.database import search_news
from datetime import datetime


# Requisito 6
# https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598
def search_by_title(title):
    news = search_news({"title": {'$regex': title, '$options': 'i'}})
    news_by_title = []
    for new in news:
        news_by_title.append((new["title"], new["url"]))
    return news_by_title


# Requisito 7
# https://acervolima.com/python-validar-formato-de-data-de-string/
def search_by_date(date):
    months_ptbr = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro',
    }
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')
    new_date = f'{date.day} de {months_ptbr[date.month]} de {date.year}'
    news = search_news({'timestamp': new_date})
    news_by_date = []
    for new in news:
        news_by_date.append((new["title"], new["url"]))
    return news_by_date


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {'$regex': tag, '$options': 'i'}})
    news_by_tag = []
    for new in news:
        news_by_tag.append((new["title"], new["url"]))
    return news_by_tag


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {'$regex': category, '$options': 'i'}})
    news_by_category = []
    for new in news:
        news_by_category.append((new["title"], new["url"]))
    return news_by_category
