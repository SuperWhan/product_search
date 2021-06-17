import requests
from bs4 import BeautifulSoup
## Setting Header for the request
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

## prefix for each shopping website
AMAZON_PREFIX = 'https://www.amazon.com'
EBAY_PREFIX = 'https://www.ebay.com'

## target item we want to compare
target = 'Monitor'

## using target item and shopping website to composing the url
amazon_url = AMAZON_PREFIX + '/s?k=' + target + '&ref=nb_sb_noss'
ebay_url = EBAY_PREFIX + '/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=' + target + '&_sacat=0'

## sending request and get response from amazon server, return html
amazon_response = requests.get(amazon_url, headers = HEADERS)
amazon_soup = BeautifulSoup(amazon_response.text, 'html.parser')

amazon_items = amazon_soup.find_all('div', attrs={'class': 's-result-item'})
name_price = []
## concatenatiing all amazon items
for item in amazon_items:
    name = item.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
    link = item.find('a', attrs={'class': 'a-link-normal a-text-normal'})
    price = item.find('span', attrs={'class': 'a-offscreen'})
    if None not in [name, price, link]:
        name_price.append([name.get_text(), AMAZON_PREFIX + link.get('href'),float(price.get_text()[1:])])

## sending request to ebay server, and get response
ebay_response = requests.get(ebay_url, headers = HEADERS)
ebay_soup = BeautifulSoup(ebay_response.text, 'html.parser')
ebay_items = ebay_soup.find_all('div', attrs={'class' : 's-item__wrapper clearfix'})
# print(ebay_items)
for item in ebay_items:
    name = item.find('h3', attrs = {'class': 's-item__title'})
    price = item.find('span', attrs = {'class': 's-item__price'})
    link = item.find('a', attrs = {'class': 's-item__link'})
    if None not in (name, price, link) and price.get_text()[0] == '$' and 'to' not in price.get_text():
        name_price.append([name.get_text(), link.get('href'), float(price.get_text()[1:])])

name_price.sort(key = lambda x: x[2])
print(name_price)
