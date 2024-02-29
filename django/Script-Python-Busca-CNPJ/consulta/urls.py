from django.urls import path
from consulta.views import consult_cnpj

urlpatterns = [
    path('', consult_cnpj, name='consult_cnpj'),
]
