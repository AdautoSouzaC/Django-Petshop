import pytest
import datetime
from model_bakery import baker
from reserva.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer

@pytest.fixtute
def dados_agendamento_errado():
     ontem = datetime,date.today() - datetime.timedelta(days=1)
     Petshop = baker.make(Petshop)
     return {
          'nome': 'nome teste',
          'email': 'email@email.com',
          'nome_pet': 'pet test',
          'data': 'ontem',
          'turno': 'manhã',
          'tamanho': 0,
          'observaçoes': '',
          'petshop': petshop.pk,
     }

@pytest.mark.django_db
def test_data_agendamento_invalido(dados_agendamento_errado):
     serelializer = AgendamentoModelSerializer(data=dados_agendamento_errado)
     assert not serelializer.is_valid()

