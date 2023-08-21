from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import CategoriaComputador, Localizacao, Computador, Fila, Chamada
from .forms import CategoriaComputadorForm, LocalizacaoForm, ComputadorForm, FilaForm, ChamadaForm

# Lista de categorias de computador
def categoria_computador_list(request):
    categorias = CategoriaComputador.objects.all()
    return render(request, 'categoria_computador_list.html', {'categorias': categorias})
# Lista de localizações
def localizacao_list(request):
    localizacoes = Localizacao.objects.all()
    return render(request, 'localizacao_list.html', {'localizacoes': localizacoes})
# Lista de categorias
def categoria_list(request):
    categorias = CategoriaComputador.objects.all()
    localizacoes = Localizacao.objects.all()
    computadores = Computador.objects.all()
    filas = Fila.objects.all()
    return render(request, 'categoria_list.html', {'categorias': categorias,'localizacoes': localizacoes,'computadores':computadores,'filas':filas,})
# Criar uma nova categoria de computador
@login_required
def categoria_computador_create(request):
    if request.method == 'POST':
        formCategoriaComputador = CategoriaComputadorForm(request.POST)
        if formCategoriaComputador.is_valid():
            categoria = formCategoriaComputador.save(commit=False)  # Não salve no banco ainda
            categoria.usuario_criador = request.user  # Defina o usuário criador
            categoria.save()  # Agora salve no banco com o usuário criador definido
            print('Salvo no banco com sucesso!!!')
            return redirect('categoria_computador_list')
    else:
        formCategoriaComputador = CategoriaComputadorForm()
    return render(request, 'categoria_computador_form.html', {'form': formCategoriaComputador})

# Criar uma nova localização
@login_required
def localizacao_create(request):
    if request.method == 'POST':
        formLocalizacaoForm = LocalizacaoForm(request.POST)
        if formLocalizacaoForm.is_valid():
            localizacao = formLocalizacaoForm.save(commit=False) 
            localizacao.usuario_criador = request.user
            localizacao.save()
            print('Salvo no banco com sucesso!!!')
            return redirect('categoria_list')
    else:
        formLocalizacaoForm = LocalizacaoForm()
    return render(request, 'localizacao_form.html', {'form': formLocalizacaoForm})
@login_required
def computador_create(request):
    if request.method == 'POST':
        formComputadorForm = ComputadorForm(request.POST)
        if formComputadorForm.is_valid():
            computador = formComputadorForm.save(commit=False) 
            computador.usuario_criador = request.user
            computador.save()
            print('Salvo no banco com sucesso!!!')
            return redirect('categoria_list')
    else:
        formComputadorForm = ComputadorForm()
    return render(request, 'Computador_Form.html', {'form': formComputadorForm})        

@login_required
def fila_create(request):
    if request.method == 'POST':
        formFilaForm = FilaForm(request.POST)
        if formFilaForm.is_valid():
            fila = formFilaForm.save(commit=False) 
            fila.usuario_criador = request.user
            fila.save()
            print('Salvo no banco com sucesso!!!')
            return redirect('categoria_list')
    else:
        formFilaForm = FilaForm()
    return render(request, 'fila_Form.html', {'form': formFilaForm})   

# Atualizar uma categoria de computador existente
def categoria_computador_update(request, pk):
    categoria = get_object_or_404(CategoriaComputador, pk=pk)
    if request.method == 'POST':
        formCategoriaComputador = CategoriaComputadorForm(request.POST, instance=categoria)
        if formCategoriaComputador.is_valid():
            formCategoriaComputador.save()
            return redirect('categoria_computador_list')
    else:
        formCategoriaComputador = CategoriaComputadorForm(instance=categoria)
    return render(request, 'categoria_computador_form.html', {'form': formCategoriaComputador})

# Atualizar uma localização existente
def localizacao_update(request, pk):
    localizacao = get_object_or_404(Localizacao, pk=pk)
    if request.method == 'POST':
        form = LocalizacaoForm(request.POST, instance=localizacao)
        if form.is_valid():
            form.save()
            return redirect('localizacao_list')
    else:
        form = LocalizacaoForm(instance=localizacao)
    return render(request, 'localizacao_form.html', {'form': form})

# Continue criando views semelhantes para Computador, Fila e Chamada
