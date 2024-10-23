import requests
from bs4 import BeautifulSoup
from tkinter import *

# Clase Scraper - Web Scraper
class Scraper:
    def __init__(self, url):
        self.url = url
    
    def scrape(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Lanza un error si la respuesta es un error HTTP

            soup = BeautifulSoup(response.content, 'html.parser')
            productos = soup.find_all('div', class_="product-container")

            resultados = []

            for producto in productos:
                nombre = producto.find('a', class_='product-name').get_text(strip=True)
                precio = producto.find('span', class_='price').get_text(strip=True) if producto.find('span', class_='price') else "No disponible"
                disponibles = producto.find('span', class_='availability').get_text(strip=True) if producto.find('span', class_='availability') else "No disponible"

                resultados.append(f"Nombre: {nombre} | Precio: {precio} | Disponibles: {disponibles}")
        
            return resultados
        
        except requests.exceptions.RequestException as e:
            return [f"Error al realizar la solicitud: {e}"]

# Clase App - Interfaz gráfica con Tkinter
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper de Productos")
        self.root.geometry("600x400")

        # Etiqueta para la URL
        self.url_label = Label(root, text="Ingrese la URL:")
        self.url_label.pack(pady=10)

        # Campo de entrada para la URL
        self.url_entry = Entry(root, width=50)
        self.url_entry.pack(pady=5)

        # Botón para iniciar el scraping
        self.scrape_button = Button(root, text="Extraer Productos", command=self.extract_products)
        self.scrape_button.pack(pady=10)

        # Área de texto para mostrar los resultados
        self.results = Text(root, wrap=WORD, height=15)
        self.results.pack(pady=10)

    def extract_products(self):
        url = self.url_entry.get()  # Obtener la URL del campo de entrada
        scraper = Scraper(url)  # Crear una instancia de Scraper
        products = scraper.scrape()  # Llamar al método de scraping

        self.results.delete(1.0, END)  # Limpiar el área de texto antes de mostrar nuevos resultados

        for product in products:
            self.results.insert(END, f'{product}\n')  # Mostrar cada producto

# Inicializar la aplicación
if __name__ == "__main__":
    root = Tk()
    app = App(root)  # Crear una instancia de App
    root.mainloop()  # Iniciar el bucle principal de la interfaz