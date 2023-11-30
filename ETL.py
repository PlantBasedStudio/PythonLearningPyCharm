#extract, transform, load.
#C'est ce qu'on utilise pour extraire et traiter des données python

# Ici on va utiliser Requests et beautiful_soup sur mon propre site web (on appelle ça "scraper")
import requests
from bs4 import BeautifulSoup

url = "https://www.kristofdetailing.fr"

response = requests.get(url) #.get() récupère le code html
html_code = response.text

print(html_code)


#L'objectif est de "parser" les élements que l'on souhaite pour récupérer des informations importantes.
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title)
print(soup.find_all('a'))
print(soup.find(classmethod="photo-page"))

