import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '75374531c45571ac94a19b89d232ef34'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change = {
    "pokemon_id": "173603",
    "name": "nbuh",
    "photo_id": 2
} 
body_catch = {
    "pokemon_id": "173603"
}
response_create = requests.post(url=f'{URL}/pokemons', headers=HEADERS, json=body_create)

print(response_create.text)
 


response_change = requests.put(url=f'{URL}/pokemons', headers=HEADERS, json=body_change)

print(response_change.text)


response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=body_catch)


print(response_catch.text)