import requests
import pytest

HOST = 'https://pokemonbattle.me:9104/'
TOKEN = 'c0163592653af4633a7466ad6062748f'

# 2. POST - Активация тренера
response_activated_trainer = requests.post(f'{HOST}trainers/confirm_email', # Имя переменной = requests.тип запроса (здесь POST)
    json={"trainer_token": TOKEN})# body запроса в формате json
print(response_activated_trainer.status_code, response_activated_trainer.text)                    # напечатать ответ переменной


# 7. PUT /trainers - Смена имени покемона
response_rename_trainer = requests.put(f'{HOST}trainers', # Имя переменной = requests.тип запроса (здесь PUT)
json={                                                      # body запроса в формате json
    'name': 'DmitryDrozd131313', 
    'city': 'Berdsk1313'
    }, 
headers= {"trainer_token": TOKEN})                         # headers запроса в формате json
print(response_rename_trainer.status_code, response_rename_trainer.text)                    # напечатать ответ переменной


# 8. GET /trainers - Получение информации по всем тренерам
response_put_trainer = requests.get(f'{HOST}trainers', # Имя переменной = requests.тип запроса (здесь GET)
params={                                                      # body запроса в формате json
    'trainer_id': 3777
    }) 
print(response_put_trainer.status_code, response_put_trainer.text)                    # напечатать ответ переменной


# 9. POST /pokemons - Создание покемона
response_create_pokemon = requests.post(f'{HOST}pokemons', # Имя переменной = requests.тип запроса (здесь POST)
json={                                                      # body запроса в формате json
    "name": "Злыдень",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
    },
    headers= {"trainer_token": TOKEN})                    # headers запроса в формате json
print(response_create_pokemon.status_code, response_create_pokemon.text)                    # напечатать ответ переменной



# 10.  GET/pokemons - Получение информации по покемонам
response_info_pokemons = requests.get(f'{HOST}pokemons', # Имя переменной = requests.тип запроса (здесь GET)
params={                                                      # body запроса в формате json
    'trainer_id': 3777
    }) 
print(response_info_pokemons.status_code, response_info_pokemons.text)                    # напечатать ответ переменной


# 11. POST /trainers/add_pokeball - Поймать покемона в покебол
response_pokemon_in_pokeball = requests.post(f'{HOST}trainers/add_pokeball', # Имя переменной = requests.тип запроса (здесь POST)
json={                                                      # body запроса в формате json
    "pokemon_id": "8997"                                      # !!! Указать id созданного покемона
    },
    headers= {"trainer_token": TOKEN})                    # headers запроса в формате json
print(response_pokemon_in_pokeball.status_code, response_pokemon_in_pokeball.text)                    # напечатать ответ переменной
