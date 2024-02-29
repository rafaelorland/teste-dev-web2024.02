from django.urls import path
from api.views import api_consultar_cnpj

urlpatterns = [
    path('consultar-cnpj/<str:cnpj>/', api_consultar_cnpj, name='api_consultar_cnpj'),
]
