import re

import requests
from bs4 import BeautifulSoup

marcos: str = "1853"
bruna: str = "1849"
pablo: str = "?"

site = f'https://www.focoradical.com.br/busca-numero?type=1&competition_id=19231&number={bruna}'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

imgs_urls = [img['data-original'] for img in img_tags if "data-original" in str(img)]

for img_url in imgs_urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', img_url)
    if not filename:
        print("Regex didn't match with the url: {url}")
        continue
    with open(filename.group(1), 'wb') as file:
        if 'http' not in img_url:
            img_url = f'{}{}'.format(site, img_url)
            print(img_url)
            print(f'{site}{img_url}')
            print(site + img_url)
        response = requests.get(img_url)
        file.write(response.content)
