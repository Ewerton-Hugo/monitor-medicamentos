from django.http import JsonResponse
from remedios.models import Remedio

def search_api(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        filtered_data = Remedio.objects.filter(campo1__icontains=query)
        results = [
            {
                'PRINCIPIO ATIVO': data.PRINCIPIO_ATIVO,
                'CNPJ': data.CNPJ,
                'LABORATORIO': data.LABORATORIO,
                'CODIGO GGREM': data.CODIGO_GGREM,
                'REGISTRO': data.REGISTRO,
                'EAN1': data.EAN1,
                'EAN2': data.EAN2,
                'EAN3': data.EAN3,
                'PRODUTO': data.PRODUTO,
                'APRESENTACAO': data.APRESENTACAO,
                'CLASSE TERAPEUTICA': data.CLASSE_TERAPEUTICA,
                'TIPO PRODUTO': data.TIPO_PRODUTO,
                'REGIME PRECO': data.REGIME_PRECO,
                'PF SEM IMPOSTOS': data.PF_SEM_IMPOSTOS,
                'PF 0': data.PF_0,
                'PF 12': data.PF_12,
                'PF 17': data.PF_17,
                'PF 17 ALC': data.PF_17_ALC,
                'PF 17 5': data.PF_17_5,
                'PF 17 5 ALC': data.PF_17_5_ALC,
                'PF 18': data.PF_18,
                'PF 18 ALC': data.PF_18_ALC,
                'PF 19': data.PF_19,
                'PF 20': data.PF_20,
                'PF 21': data.PF_21,
                'PF 22': data.PF_22,
                'PMVG SEM IMPOSTOS': data.PMVG_SEM_IMPOSTOS,
                'PMVG 0': data.PMVG_0,
                'PMVG 12': data.PMVG_12,
                'PMVG 17': data.PMVG_17,
                'PMVG 17 ALC': data.PMVG_17_ALC,
                'PMVG 17 5': data.PMVG_17_5,
                'PMVG 17 5 ALC': data.PMVG_17_5_ALC,
                'PMVG 18': data.PMVG_18,
                'PMVG 18 ALC': data.PMVG_18_ALC,
                'PMVG 19': data.PMVG_19,
                'PMVG 20': data.PMVG_20,
                'PMVG 21': data.PMVG_21,
                'PMVG 22': data.PMVG_22,
                'RESTRICAO HOSPITALAR': data.RESTRICAO_HOSPITALAR,
                'CAP': data.CAP,
                'CONFAZ 87': data.CONFAZ_87,
                'ICMS 0': data.ICMS_0,
                'ANALISE_RECURSAL': data.ANALISE_RECURSAL,
                'LISTA CONCESSAO CREDITO': data.LISTA_CONCESSAO_CREDITO,
                'COMERCIALIZACAO 2022': data.COMERCIALIZACAO_2022,
                'TARJA': data.TARJA,
            }
            for data in filtered_data
        ]

        return JsonResponse(results, safe=False)