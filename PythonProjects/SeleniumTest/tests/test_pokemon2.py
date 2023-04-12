import requests
import pytest

TOKEN = 'c0163592653af4633a7466ad6062748f'

@pytest.mark.parametrize('key, value', [('trainer_name', 'DmitryDrozd1313'), ('city', 'Berdsk13'), 
                                        ('id', '3777')])
def test_parts_of_body(key, value):
    response_parts_of_body = requests.get('https://pokemonbattle.me:9104/trainers', 
    params= {'trainer_id': 3777})
    assert response_parts_of_body.json()[key] == value


@pytest.mark.parametrize('key, value', [('status', '1'), ('trainer_id', '3777'), 
                                        ('attack', '1.0'), ('name', 'Злыдень')])
def test_put_trainer(key, value):
    response_put_trainer = requests.get('https://pokemonbattle.me:9104/pokemons', 
    params= {'pokemon_id': 8978})
    assert response_put_trainer.json()[key] == value