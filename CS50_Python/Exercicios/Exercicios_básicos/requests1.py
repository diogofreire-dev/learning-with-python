import requests
import json

url = "https://api.chucknorris.io/jokes/random"

try:
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        # Conveter a resposta para formato JSON
        dados = resposta.json()
        
        # Exibir a piada
        print("Anedota do Chuck Norris:")
        print(dados["value"])
    else:
        print(f"Erro na requisição: {resposta.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")