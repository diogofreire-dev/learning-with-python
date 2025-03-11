import json
import requests

nome = input("Insira o nome do artista: ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + nome)

o = response.json()
for result in o["results"]:
    print(result["trackName"])

# Output : The track names of the 50 songs that match the search term