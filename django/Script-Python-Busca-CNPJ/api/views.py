from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.service import valida_cnpj
from rest_framework import status
import requests


@api_view(['GET'])
@permission_classes([AllowAny])
def api_consultar_cnpj(request, cnpj):
    if valida_cnpj(cnpj):
        response_api_cnpj = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}')

        if response_api_cnpj.status_code == 200:
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

            return Response(dados_processados)
        else:
            return Response({"error": "Falha ao consultar CNPJ"}, status=response_api_cnpj.status_code)
    else:
        return Response({"error": "Os dígitos verificadores estão incorretos."}, status=status.HTTP_400_BAD_REQUEST)