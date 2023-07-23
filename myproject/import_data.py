# myproject/import_data.py
import os
import django

# Configurar o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()


def import_data():
    with open('xls_conformidade_gov.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # PRINCIPIO_ATIVO, CNPJ, LABORATORIO, CODIGO_GGREM, REGISTRO, EAN1, EAN2, EAN3, PRODUTO, APRESENTACAO, CLASSE_TERAPEUTICA, TIPO_PRODUTO, REGIME_PRECO, PF_SEM_IMPOSTOS, PF_0, PF_12, PF_17, PF_17_ALC, PF_17_5, PF_17_5_ALC, PF_18, PF_18_ALC, PF_19, PF_20, PF_21, PF_22, PMVG_SEM_IMPOSTOS, PMVG_0, PMVG_12, PMVG_17, PMVG_17_ALC, PMVG_17_5, PMVG_17_5_ALC, PMVG_18, PMVG_18_ALC, PMVG_19, PMVG_20, PMVG_21, PMVG_22, RESTRICAO_HOSPITALAR, CAP, CONFAZ_87, ICMS_0, ANALISE_RECURSAL, LISTA_CONCESSAO_CREDITO, COMERCIALIZACAO_2022, TARJA = row

            # Agora você pode usar os valores das novas colunas para criar e salvar o objeto Item no banco de dados
            Dados.objects.create(
                PRINCIPIO_ATIVO=row['PRINCIPIO ATIVO'],
                CNPJ=row['CNPJ'],
                LABORATORIO=row['LABORATORIO'],
                CODIGO_GGREM=row['CODIGO GGREM'],
                REGISTRO=row['REGISTRO'],
                EAN1=row['EAN1'],
                EAN2=row['EAN2'],
                EAN3=row['EAN3'],
                PRODUTO=row['PRODUTO'],
                APRESENTACAO=row['APRESENTACAO'],
                CLASSE_TERAPEUTICA=row['CLASSE TERAPEUTICA'],
                TIPO_PRODUTO=row['TIPO PRODUTO'],
                REGIME_PRECO=row['REGIME PRECO'],
                PF_SEM_IMPOSTOS=row['PF SEM IMPOSTOS'],
                PF_0=row['PF 0'],
                PF_12=row['PF 12'],
                PF_17=row['PF 17'],
                PF_17_ALC=row['PF 17 ALC'],
                PF_17_5=row['PF 17 5'],
                PF_17_5_ALC=row['PF 17 5 ALC'],
                PF_18=row['PF 18'],
                PF_18_ALC=row['PF 18 ALC'],
                PF_19=row['PF 19'],
                PF_20=row['PF 20'],
                PF_21=row['PF 21'],
                PF_22=row['PF 22'],
                PMVG_SEM_IMPOSTOS=row['PMVG SEM IMPOSTOS'],
                PMVG_0=row['PMVG 0'],
                PMVG_12=row['PMVG 12'],
                PMVG_17=row['PMVG 17'],
                PMVG_17_ALC=row['PMVG 17 ALC'],
                PMVG_17_5=row['PMVG 17 5'],
                PMVG_17_5_ALC=row['PMVG 17 5 ALC'],
                PMVG_18=row['PMVG 18'],
                PMVG_18_ALC=row['PMVG 18 ALC'],
                PMVG_19=row['PMVG 19'],
                PMVG_20=row['PMVG 20'],
                PMVG_21=row['PMVG 21'],
                PMVG_22=row['PMVG 22'],
                RESTRICAO_HOSPITALAR=row['RESTRICAO HOSPITALAR'],
                CAP=row['CAP'],
                CONFAZ_87=row['CONFAZ 87'],
                ICMS_0=row['ICMS 0'],
                ANALISE_RECURSAL=row['ANALISE RECURSAL'],
                LISTA_CONCESSAO_CREDITO=row['LISTA CONCESSAO CREDITO'],
                COMERCIALIZACAO_2022=row['COMERCIALIZACAO 2022'],
                TARJA=row['TARJA'],
            )
            Dados.save()
