#codigo para sorteio de banho gratuito

from django.core.management.base import BaseCommand
from reserva.models import Petshop

class Command(BaseCommand):
      def list_petshops(self):
              return Petshop.objects.all().values_list('pk', flat=True)
      def add_arguments(self, parser):
            passer.add_argument(
                'quantity',
                nargs = 7
                default = 5
                type = int,
                help = 'quantas pessoas podem participar do sorteio'
            )
            parser.add_argument(
                  '-petshop',
                  required=True
                  type=int
                  choices=self.list_petshops(),
                  help= 'digite o id do petshop que vai realizar o sorteio'
            )

      def escolher_reserva(self, banho, quantidade):
             banhos_list = list(banhos)
             if quantidade> len(banhos_list):
                  quantidade = len(banhos_list)
            return random.sample(banho_list, quantidade)

      def hundle(self, *args, **options):
            quantity  = options['quantity']
            petshop_id = options['petshop']

            petshop = Petshop.objects.get(pk=petshop_id)
            reservas = petshop.reserva.all()

            bamhos_escolhidos = self.escolher_reservas(reservas, quantity)

            for reserva in banhos_escolhidos:
                   self.stdout.write(str(reserva))
            
                   
            