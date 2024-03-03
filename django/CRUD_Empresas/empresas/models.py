from django.db import models

class Empresa(models.Model):
    razao_social = models.CharField(max_length=200, verbose_name='Razão Social')
    atividade_principal = models.CharField(max_length=200, verbose_name='Atividade Principal')
    numero_endereco = models.CharField(max_length=20, verbose_name='Número do Endereço')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    municipio = models.CharField(max_length=100, verbose_name='Município')
    estado = models.CharField(max_length=50, verbose_name='Estado')

    def __str__(self):
        return self.razao_social

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
