from bs4 import BeautifulSoup
import requests, lxml


headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}


def get_prices(camera):
    headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
    
    html = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={camera}&_sacat=0, headers=headers').text
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
    return average