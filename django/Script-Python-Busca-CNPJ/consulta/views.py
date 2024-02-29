from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .service import valida_cnpj
import requests

def consult_cnpj(request):
    if request.method == 'POST':
        # cnpj da requisição POST
        cnpj_request = request.POST.get('cnpj')

        # tirando caracteres do cnpj
        cnpj_sem_caracter = ''.join(filter(str.isdigit, cnpj_request))

        #validando cnpj
        if valida_cnpj(cnpj_sem_caracter):
            response_api_cnpj = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj_sem_caracter}')

            # processando dados para a resposta
            data = response_api_cnpj.json()

            dados_processados = {
                "razao_social": data.get('nome'),
                "codigo_atividade_principal": data['atividade_principal'][0]['code'],
                "endereco": {
                    "numero": data.get("numero"),
                    "cep": data.get("cep"),
                    "municipio": data.get("municipio"),
                    "estado": data.get("uf"),
                }
            }

            return render(request, 'components/response_cnpj.html', dados_processados)
        else:
            messages.info(request, f"CNPJ: {cnpj_request} é inválido.")

    return render(request, 'page/consultar_cnpj.html')