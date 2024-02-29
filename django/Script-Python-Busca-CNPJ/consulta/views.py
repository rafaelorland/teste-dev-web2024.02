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
            dados_processados = {
                "razao_social": response_api_cnpj.json().get('nome'),
                "codigo_atividade_principal": response_api_cnpj.json()['atividade_principal'][0]['code'],
                "endereco": {
                    "numero": response_api_cnpj.json().get("numero"),
                    "cep": response_api_cnpj.json().get("cep"),
                    "municipio": response_api_cnpj.json().get("municipio"),
                    "estado": response_api_cnpj.json().get("uf"),
                }
            }

            return render(request, 'components/response_cnpj.html', dados_processados)
        else:
            messages.info(request, f"CNPJ: {cnpj_request} é inválido.")

    return render(request, 'page/consultar_cnpj.html')