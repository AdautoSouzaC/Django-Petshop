from datetime import date
import pytest
from model_bakery import baker
from reserva.models import Reserva


#FIXTURE
@pytest.fixture
def reserva():
    reserva = baker.make(
        Reserva,
        nome = 'Tom',
        data =date.today(),
        turno = 'Tarde'
    )
    return reserva


@pytest.mark.django.db
def test_reserva_deve_retornar_string_formata():
    assert str(reserva) == 'tom: 2023-07-12 - Tarde'