import requests
from bs4 import BeautifulSoup
import os

url="https://www.kaggle.com/datasets"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

datasets = soup.find_all('house predictions')
print(datasets)