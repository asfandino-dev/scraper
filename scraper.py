import requests
from bs4 import BeautifulSoup

url = "https://www.electronicoscaldas.com/es/buscar?controller=search&orderby=position&orderway=desc&search_query=microcontrolador+pic&submit_search="

response =requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

productos = soup.find_all('div', class_="product-container")

for producto in productos:
    nombre = producto.find('a',class_='product-name').get_text(strip=True)
    precio = producto.find('span',class_='price').get_text(strip=True)
    disponibles = producto.find('span', class_='availability').get_text(strip=True)

    print(f"Nombre: {nombre} | Precio: {precio} | Disponibles: {disponibles}")