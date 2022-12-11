from bs4 import BeautifulSoup
import requests
import statistics

def get_prices(camera):   
    #inserting the camera name to a search link to scrape below    
    search_link = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={camera}&_sacat=0&rt=nc&LH_BIN=1'
    
    #searching here
    html = requests.get(f'{search_link}, headers=headers').text
    soup = BeautifulSoup(html, 'lxml')

    #sorting through data for each ebay intem and adding the price to the 'data' list, then converting to integers
    data = []
    for item in soup.select('.s-item__wrapper.clearfix'):
        try:
            price = item.select_one('.s-item__price').text
            price_as_int = (int(float(price[1:])))
            data.append(price_as_int)
        except:
            pass
    
    #taking the average from the data list and then removing any value higher than the standard deviation of that list.
    #Some values are unusually high, typically for cameras that are unboxed and way above the normal price. This is done to sort those out
    average = statistics.mean(data)
    std_dev = statistics.stdev(data)
    for i in data:
        if i > average + std_dev:
            data.remove(i)
            
    #calculating a new average.
    average = round(statistics.mean(data))
    
    return {'average_price': average,
            'link': search_link}