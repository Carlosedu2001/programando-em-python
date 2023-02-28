import os
import requests

os.system("cls")

API_KEY = input("Digite sua chave para validação: ")

cidade = input("Qual cidade deseja saber o clima? ")

cordenadas = f'http://api.openweathermap.org/geo/1.0/direct?q={cidade}&limit={1}&appid={API_KEY}&lang=pt_br'

response_cordenadas = requests.get(cordenadas)
info_cordenadas = response_cordenadas.json()

lat = info_cordenadas[0]['lat']
lon = info_cordenadas[0]['lon']

clima_cidade = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=pt_br'

response_clima = requests.get(clima_cidade)
info_clima = response_clima.json()

descricao = info_clima['weather'][0]['description']
temperatura = info_clima['main']['temp']-273.15

print(f"\nEm {cidade} o clima está {descricao} com uma temperatura de {int(temperatura)}ºC")