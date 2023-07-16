
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
    pattern1 = r'^\/national'
    pattern2 = r'^/international'

    for str_ in array:
        if re.findall(pattern1, str_) or re.findall(pattern2, str_):
            result.append(str_)

    return result


def giant_process(list):
    """This is the big process where i have to scrap"""
    page_url = BASE_URL + list[3]

    print(page_url)
    # soup = proxy_request(page_url)
    # print(soup)


    """
    for i,page in enumerate(list):
        page_url = BASE_URL + page

        print(i, page_url)
    """

if __name__ == '__main__':
    soup = proxy_request(BASE_URL)
    myUrls = soup.find_all('a')

    urls = filter_1([url.get('href') for url in myUrls if url.get('href')])

    giant_process(urls)
    print(len(urls))

