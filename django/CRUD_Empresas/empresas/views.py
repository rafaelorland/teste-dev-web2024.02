import json
from django.shortcuts import get_object_or_404, render,HttpResponse
from .models import Empresa

# HOME PAGE
def home_page(request):
    context = {
        "total_empresa": Empresa.objects.count()
    }
    return render(request, 'home_page.html', context)
    
# READ
def visualizar_empresa(request):
    if request.method == 'POST':
        pesquisa = request.POST.get('pesquisa')

        resultado_pesquisa = Empresa.objects.filter(razao_social__icontains=pesquisa)

        return render(request, 'pages/pesquisar_empresas.html', {"empresas": resultado_pesquisa})

    context = {
        "empresas": Empresa.objects.all()
    }
    return render(request, 'pages/pesquisar_empresas.html', context)

# UPDATE
def modificar_empresa(request):
    context = {
        "index_url": "modificar",
        "titulo": "modificar",
        "empresas": Empresa.objects.all()
    }
    return render(request, 'components/selecionar_empresa.html', context)

# UPDATE
def modificar(request, id_empresa):
    empresa = get_object_or_404(Empresa, pk=id_empresa)

    if request.method == 'POST':
        try:
            razao_social        = request.POST.get('razao_social')
            atividade_principal = request.POST.get('atividade_principal')
            numero_endereco     = request.POST.get('numero_endereco')
            cep                 = request.POST.get('cep')
            municipio           = request.POST.get('municipio')
            estado              = request.POST.get('estado')

            if razao_social and atividade_principal and numero_endereco and cep and municipio and estado:

                empresa.razao_social = razao_social
                empresa.atividade_principal = atividade_principal
                empresa.numero_endereco = numero_endereco
                empresa.cep = cep
                empresa.municipio = municipio
                empresa.estado = estado

                empresa.save()

                context = {
                        "razao_social":               razao_social,
                        "codigo_atividade_principal": atividade_principal,
                        "numero":                     numero_endereco,
                        "cep":                        cep,
                        "municipio":                  municipio,
                        "estado":                     estado,
                        "index":                      "modificada"
                    }

                return render(request, 'components/sucess.html', context)
            
            else:

                return render(request, 'components/error.html', {'error':'preencha todo o formulário'})
            
        except Exception as e:

            return render(request, 'components/error.html', {'error': e})

    dados_atual_empresa = {
        "razao_social":        empresa.razao_social,
        "atividade_principal": empresa.atividade_principal,
        "numero_endereco":     empresa.numero_endereco,
        "cep":                 empresa.cep,
        "municipio":           empresa.municipio,
        "estado":              empresa.estado
    }

    return render(request, 'pages/modificar.html', dados_atual_empresa)

# CREATE
def adicionar_empresa(request):
    if  request.method  == 'POST':
        razao_social        = request.POST.get('razao_social')
        atividade_principal = request.POST.get('atividade_principal')
        numero_endereco     = request.POST.get('numero_endereco')
        cep                 = request.POST.get('cep')
        municipio           = request.POST.get('municipio')
        estado              = request.POST.get('estado')

        if razao_social and atividade_principal and numero_endereco and cep and municipio and estado:
            empresa = Empresa(razao_social= razao_social,atividade_principal= atividade_principal,numero_endereco= numero_endereco,cep= cep,municipio= municipio,estado= estado)
            empresa.save()
            context = {
                "razao_social":               razao_social,
                "codigo_atividade_principal": atividade_principal,
                "numero":                     numero_endereco,
                "cep":                        cep,
                "municipio":                  municipio,
                "estado":                     estado,
                "index":                      "salva"
            }
            return render(request, 'components/sucess.html', context)
        else:
            return render(request, 'components/error.html', {'error':'preencha o formulário'})
        
    return render(request, 'pages/adicionar_empresa.html')

def excluir_empresa(request):
    context = {
        "index_url": "excluir",
        "titulo": "excluir",
        "empresas": Empresa.objects.all()
    }
    return render(request, 'components/selecionar_empresa.html', context)

def excluir(request, id_empresa):
    empresa = get_object_or_404(Empresa, pk=id_empresa)
    if request.method == 'POST':
        context = {
            "razao_social":               empresa.razao_social,
            "codigo_atividade_principal": empresa.atividade_principal,
            "numero":                     empresa.numero_endereco,
            "cep":                        empresa.cep,
            "municipio":                  empresa.municipio,
            "estado":                     empresa.estado,
            "index":                      "excluída"
                    }
        empresa.delete()
        return render(request, 'components/sucess.html', context)
    return render(request, 'components/confirm_delete_empresa.html', {"empresa": empresa})