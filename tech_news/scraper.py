import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url=url, headers={"user-agent": "Fake user-agent"}, timeout=3)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = selector.css("h2.entry-title > a::attr(href)").getall()
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    result = selector.css("div.nav-links > a.next::attr(href)").get()
    return result


# Requisito 4
# https://parsel.readthedocs.io/en/latest/usage.html
# https://www.delftstack.com/pt/howto/python/python-extract-number-from-string/#:~:text=Utilizar%20a%20Compreens%C3%A3o%20da%20Lista,%C3%A9%20encontrado%20atrav%C3%A9s%20da%20itera%C3%A7%C3%A3o.
# noticia com comentarios:
# https://blog.betrybe.com/framework-de-programacao/o-que-e-framework/#comment-376
# https://docs.scrapy.org/en/latest/topics/selectors.html
def scrape_noticia(html_content):
    selector = Selector(html_content)
    str_comments = selector.css("h5.title-block::text").get()
    comments = [int(temp)for temp in str_comments.split() if temp.isdigit()]
    dic_noticia = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author > a::text").get(),
        "comments_count": comments[0] if len(comments) > 0 else 0,
        "summary": selector.xpath("string(//div['entry-content']/p)").get(),
        "tags": selector.css("section.post-tags a::text").getall(),
        "category": selector.css("a.category-style > span.label::text").get(),
    }
    return dic_noticia


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
