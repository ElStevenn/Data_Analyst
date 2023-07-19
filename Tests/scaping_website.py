
"""
Here, as you can see I'm scaping a website
"""
import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd

cls = lambda: os.system('cls')
cls()

BASE_URL = 'https://es.soccerway.com/'
url = BASE_URL + ''

Total_Data = {}
username, password = 'astevee','TusMuertos777'


def proxy_request(url):
    """With this function I use a proxy to axcess to some websites."""
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

def filter_1(array):
    result = []
    pattern1 = r'^/national'
    pattern2 = r'^/international'

    for str_ in array:
        if re.findall(pattern1, str_) or re.findall(pattern2, str_):
            result.append(str_)

    return result


def giant_process(list):
    """This is the big process where i have to scrap"""
    page_url = BASE_URL + list[3]
    legues = []
    
    soup = proxy_request(page_url)

    filter_1 = soup.find('div', {'id':'subheading'})
    print(filter_1.text.split()[0])
    
    
    for page in list[:10]:
        page_url = BASE_URL + page
        soup = proxy_request(page_url)
        
        # Get Name
        filter_1 = soup.find('h1') # ,{'id':'subheading'}
        to_append = filter_1.text.strip()
        legues.append(to_append)

        


        print("- " + str(to_append) + " crawled!")

    print(legues)
    
    

if __name__ == '__main__':
    soup = proxy_request(BASE_URL)
    myUrls = soup.find_all('a')

    urls = filter_1([url.get('href') for url in myUrls if url.get('href')])

    giant_process(urls)
    print(len(urls))

