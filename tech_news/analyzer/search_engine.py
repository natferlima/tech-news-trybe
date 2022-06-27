from tech_news.database import search_news


# Requisito 6
# https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598
def search_by_title(title):
    news = search_news({"title": {'$regex': title, '$options': 'i'}})
    news_by_title = []
    for new in news:
        news_by_title.append((new["title"], new["url"]))
    return news_by_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


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
