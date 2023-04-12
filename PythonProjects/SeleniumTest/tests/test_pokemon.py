import requests
import pytest

TOKEN = 'c0163592653af4633a7466ad6062748f'
#HOST = https://pokemonbattle.me:9104/


# Создание покемона и проверка статус-кода
def test_status_code():
    response_status_code = requests.post('https://pokemonbattle.me:9104/pokemons', # Имя переменной = requests.тип запроса (здесь POST)
    json={                                                      # body запроса в формате json
    "name": "Злыдень-8",
    "photo": "https://dolnikov.ru/pokemons/albums/006.png"
    },
    headers= {"trainer_token": TOKEN})
    assert response_status_code.status_code == 400                  # Утверждаю, что статус-код будет 400

def test_part_of_body():
    response_part_of_body = requests.get('https://pokemonbattle.me:9104/trainers',
    params={                                                      # qwery запроса в формате json
    'trainer_id': 3777
    })  
    #response_part_of_body.body = response_part_of_body.text    #- Нужно или нет?
    assert response_part_of_body.json()['trainer_name'] == 'DmitryDrozd1313'

def test_activated_trainer(): 
    response_activated_trainer = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', # Имя переменной = requests.тип запроса (здесь POST)
    json={"trainer_token": TOKEN})# body запроса в формате json
    assert response_activated_trainer.status_code == 400
    assert response_activated_trainer.json()['message'] == 'Аккаунт уже подтверждён'
    assert response_activated_trainer.json()['status'] == 'error'

def test_rename_trainer():
    response_rename_trainer = requests.put('https://pokemonbattle.me:9104/trainers', # Имя переменной = requests.тип запроса (здесь PUT)
    json={                                                      # body запроса в формате json
    'name': 'DmitryDrozd1313', 
    'city': 'Berdsk13'
    }, 
    headers= {"trainer_token": TOKEN})
    assert response_rename_trainer.status_code == 200
    assert response_rename_trainer.json()['message'] == 'Информация о тренере обновлена'
    assert response_rename_trainer.json()['id'] == '3777'

def test_put_trainer():
    response_put_trainer = requests.get('https://pokemonbattle.me:9104/trainers', # Имя переменной = requests.тип запроса (здесь GET)
    params={                                                      # body запроса в формате json
    'trainer_id': 3777
    }) 
    assert response_put_trainer.status_code == 200
    assert response_put_trainer.json()['city'] == 'Berdsk13'
    assert response_put_trainer.json()['pokemons_alive'] == ["8915","8976","8977","8978","8997"]