from django.core.management.base import BaseCommand
from model_bakery import baker

from reserva.models import Reserva

class Command(BaseCommand):
    help = 'cria dados fake para testar api'

    def handle(self,*args, **options):
        total = 50
        self.stdout.write(
            self.style.WARNING(f'criando {total} agendamentos')
        )
        for i in range(total):
            reserva = baker.make(Reserva)
            reserva.save()
        self.stdout.write(
            self.style.SUCCESS('Agendamentoscriados')
        )