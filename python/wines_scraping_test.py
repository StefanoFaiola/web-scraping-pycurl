import pycurl
import certifi
from io import BytesIO
import json
import pandas as pd
import gc
import psutil
import time

n = 0
wave = 1
pages_available = True
wines_collection = []
wine_keys = set()

print("Scraping Started")
while pages_available:
    buffer = BytesIO()
    curl = pycurl.Curl()
    url = f'https://www.vivino.com/api/explore/explore?country_code=IT&currency_code=EUR&grape_filter=varietal&min_rating=1&order_by=price&order=desc&price_range_max=0&price_range_min=0&page={n}&language=en'
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0")
    curl.setopt(pycurl.WRITEDATA, buffer)
    curl.setopt(pycurl.CAINFO, certifi.where())
    curl.perform()

    if curl.getinfo(pycurl.RESPONSE_CODE) == 200:
        curl.close()
        page_dict = json.loads(buffer.getvalue().decode())
        n += 1
        
        for i in page_dict['explore_vintage']['matches']:
            if i['vintage']['id'] not in wine_keys:
                i['web.page'] = n
                wines_collection.append(i)
                wine_keys.add(i['vintage']['id'])        
    else:
        pages_available = False
        pd.json_normalize(wines_collection).to_csv(f'Wave{wave}.csv', index = False)
        print(f'Not Success{curl.getinfo(pycurl.RESPONSE_CODE)}, last page: {n}')
    print(f'Wave {wave}, {len(wines_collection)}, {n}')
print("Script excecuted succesfully")