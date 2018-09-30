import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
with open("newyorktimes_test.txt", "w+") as ny_times:
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('span', attrs={'class':'short-desc'})
    records = []
    for result in results:
        date = str(result.find('strong').text[0:-1]) + ', 2017'
        lie = str(result.contents[1][1:-2])
        explanation = str(result.contents[2].text) 
        url = str(result.find('a')['href']) 
        records.append((date, lie, explanation, url))
    ny_times.write("\n".join(records))