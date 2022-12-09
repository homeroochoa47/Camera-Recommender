from bs4 import BeautifulSoup
import requests, json, lxml

headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}


def get_prices():
    html = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=nikon+fe&_sacat=0&Model=Nikon%2520FE&_dcat=15230&rt=nc&LH_BIN=1', headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    data = []

    for item in soup.select('.s-item__wrapper.clearfix'):
        title = item.select_one('.s-item__title').text
        link = item.select_one('.s-item__link')['href']
        try:
            price = item.select_one('.s-item__price').text
        except:
            price = None
        data.append(price
            
            )
    camera_prices = []

    for i in data:
        try:
            camera_prices.append(int(float(i[1:])))
        except:
            pass

    average = int(sum(camera_prices) / len(camera_prices))
    print (average)



get_organic_results() 