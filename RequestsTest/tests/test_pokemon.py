import requests
import pytest

def test_status_code():
    response = requests.get('https://api.pokemonbattle.ru/v2/trainers')
    assert response.status_code == 200

def test_piece_body():
    response = requests.get('https://api.pokemonbattle.ru/v2/trainers', params={'trainer_id': '12851'}).json()
    trainer_name = response['data'][0]['trainer_name']
    assert trainer_name == 'Тигр'

