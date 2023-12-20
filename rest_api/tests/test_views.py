import pytest
from rest_framework.test import APIClient
import datetime
from reserva.models import Petshop, Reserva
from rest_api.serializers import PetshopModelSerializer
from model_bakery import baker
#teste para salvar agendamento de banhos
@pytest.fixture
def dados_agendamento():
    hoje = datetime.datetime.today()
    Petshop = baker.make(Petshop)
    return{
        'nome': 'nome teste',
        'nome_pet': 'pet teste',
        'data': hoje,
        'turno': 'manhã',
        'tamanho': '0',
        'observacoes': '',
        'petshop': Petshop,
    }
@pytest.mark.django_db
def teste_criar_agendamento(dados_agendamento):
    cliente = APIClient()
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    assert resposta.status_code == 201
    
@pytest.mark.django_db
def test_todos_petshop(dados_agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/petshop',)
    assert len(resposta.data['results']) ==0