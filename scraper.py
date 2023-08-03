#Importamos las bibliotecas necesarias
import requests
from bs4 import BeautifulSoup

#Obtenemos el contenido de la página web con request
url = input("Ingrese la URL del sitio web: ")
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print("Error al acceder a la página:", response.status_code)
    exit()

#Analizamos el HTML con BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

#Extraemos citas de los autores
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

#Mostramos los datos en la consola
for i in range(len(quotes)):
    print(f"\"{quotes[i].text}\" - {authors[i].text}")