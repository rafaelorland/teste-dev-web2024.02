from django.urls import path
from .views import home_page, adicionar_empresa, visualizar_empresa, modificar_empresa, modificar, excluir_empresa, excluir

urlpatterns = [
    path('', home_page, name='home_page'),
    path('adicionar-empresa/', adicionar_empresa, name='adicionar_empresa'),
    path('visualizar-empresas/', visualizar_empresa, name='visualizar_empresas'),
    path('modificar-empresa/',modificar_empresa , name='modificar_empresa'),
    path('modificar/<int:id_empresa>',modificar , name='modificar'),
    path('excluir-empresa/',excluir_empresa , name='excluir_empresa'),
    path('excluir/<int:id_empresa>',excluir , name='excluir'),
]
