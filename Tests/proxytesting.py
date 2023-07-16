# import proxy
import requests
from bs4 import BeautifulSoup
""" What's the idea behind via proxy?"""
# The main problem is that when we try to connect to a server the most
# probably is that our ip is blocked 

"""We star here"""
BASE_URL = 'https://books.toscrape.com/'

url = BASE_URL + ''
username, password = 'astevee','TusMuertos777'

def proxy_request(url):
    """I get the data using a proxy"""
    payload = {
        'source': 'universal',
        'url': url,
        'geo_location': 'Germany',
    }

    response = requests.request(
        "POST", "https://realtime.oxylabs.io/v1/queries",
        auth = (username, password),
        json = payload
    )

   
    response_html = response.json()['results'][0]['content']
    return BeautifulSoup(response_html , 'lxml')




soup = proxy_request(BASE_URL)



"""
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
"""
price_tags = soup.find_all("p", {"class":"price_color"})
names = soup.find_all("article", {"class": "product_pod"})


all_prices = [float(price.text[1:]) for price in price_tags]
print(all_prices)


# When we use a proxy, we get a diferent html with differents simbols and something more





# curl 'https://realtime.oxylabs.io/v1/queries' --user 'astevee:TusMuertos777' -H 'Content-Type: application/json' -d '{"source": "universal", "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html", "geo-location": "United States", "render": "html"}' -v 
# curl 'http://quotes.toscrape.com/js/' -U 'astevee:TusMuertos777' -x 'unblock.oxylabs.io:60000' -H 'x-oxylabs-geo-location: United States' -H 'x-oxylabs-render: html' -k -v 


