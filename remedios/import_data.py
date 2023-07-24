import csv
from django.core.management.base import BaseCommand

from remedios.models import Remedio
class Command(BaseCommand):
    help = 'Importa dados de um arquivo CSV para o banco de dados'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                nome = row['nome']
                descricao = row['descricao']
                preco = row['preco']
                Remedio.objects.create(nome=nome, descricao=descricao, preco=preco)
        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))
