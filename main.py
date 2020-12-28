import requests
from bs4 import  BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (hp Elitebook 8440p) Gecko/20100101 Firefox/55.0',
}
url = "https://www.agtta.co.in/individuals.php"
r = requests.get(url, headers=headers)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent, "html.parser")
#print(soup.prettify)

text = soup.get_text()

df = pd.DataFrame([text])
df.to_csv('drivers.csv', index=True, encoding='utf-8')