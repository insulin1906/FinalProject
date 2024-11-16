import aiohttp
from bs4 import BeautifulSoup


BASE_URL = "https://www.wildberries.ru"


async def fetch_html(session, url):
    async with session.get(url) as response:
        return await response.text()


async def search_products(query):
    search_url = f"{BASE_URL}/catalog/0/search.aspx?search={query}"
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(session, search_url)
        soup = BeautifulSoup(html, 'html.parser')

        products = []
        for item in soup.select('.product-card'):
            title = item.select_one('.goods-name').text.strip()
            price = item.select_one('.price-current').text.strip()
            link = BASE_URL + item.select_one('a')['href']
            products.append({
                "title": title,
                "price": price,
                "link": link
             })

        return products
