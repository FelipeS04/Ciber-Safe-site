from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseForbidden
from .models import Topic, Entry, Noticia, Servico, Comentario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import TopicSerializer, EntrySerializer, NoticiaSerializer
from .forms import FormularioDeRegistro, ComentarioForm

def index(request):
    """Página principal que exibe notícias organizadas por categoria"""
    
    # Obtém todas as categorias distintas
    categorias = Noticia.objects.values_list('categoria', flat=True).distinct()
    
    # Organiza as notícias por categoria
    noticias_por_categoria = {}
    for categoria in categorias:
        noticias_por_categoria[categoria] = Noticia.objects.filter(categoria=categoria).order_by('-data_publicacao')
    
    # Passa as notícias por categoria para o template
    return render(request, 'learning_logs/index.html', {'noticias_por_categoria': noticias_por_categoria})

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def register(request):
    if request.method == 'POST':
        form = FormularioDeRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioDeRegistro()
    return render(request, 'learning_logs/register.html', {'form': form})

def noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    comentarios = noticia.comentarios.order_by('-criado_em')
    
    noticias_mesma_categoria = Noticia.objects.filter(
        categoria=noticia.categoria
    ).exclude(pk=pk).order_by('-data_publicacao')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            comentario.autor = request.user
            comentario.save()
            return redirect('noticia', pk=noticia.id)
    else:
        form = ComentarioForm()

    context = {
        'noticia': noticia,
        'noticias_mesma_categoria': noticias_mesma_categoria,
        'comentarios': comentarios,
        'form': form
    }

    return render(request, 'learning_logs/noticia.html', context)

def sobre(request):
    return render(request, 'learning_logs/sobre.html')

def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'learning_logs/servicos.html', {'servicos': servicos})

def servico(request):
    return render(request, 'learning_logs/erro.html')

def cursos(request):
    return render(request, 'learning_logs/cursos.html')

def curso_01(request):
    return render(request, 'learning_logs/curso_01.html')

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-date_added')
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('-date_added')
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all().order_by('-data_publicacao')
    serializer_class = NoticiaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

@login_required
def adicionar_comentario(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.noticia = noticia
            comentario.save()
    return redirect('noticia', pk=pk)

@login_required
def editar_comentario(request, pk, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id, noticia__pk=pk)
    
    if request.user != comentario.autor:
        return HttpResponseForbidden("Você não tem permissão para editar este comentário.")
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('noticia', kwargs={'pk': pk})}#comentario-{comentario.pk}")

    else:
        form = ComentarioForm(instance=comentario)

    noticia = comentario.noticia
    comentarios = noticia.comentarios.order_by('-criado_em')
    noticias_mesma_categoria = Noticia.objects.filter(
        categoria=noticia.categoria
    ).exclude(pk=pk).order_by('-data_publicacao')

    context = {
        'noticia': noticia,
        'comentarios': comentarios,
        'noticias_mesma_categoria': noticias_mesma_categoria,
        'comentario_em_edicao': comentario,
        'form_edicao': form,
        'form': ComentarioForm(),  # Form de novo comentário
    }
    return render(request, 'learning_logs/noticia.html', context)

@login_required
def excluir_comentario(request, pk, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id, noticia__pk=pk)
    
    if request.user != comentario.autor:
        return HttpResponseForbidden("Você não tem permissão para excluir este comentário.")
    
    if request.user == comentario.autor:
        noticia_id = comentario.noticia.id
        comentario.delete()
        return redirect(f"{reverse('noticia', kwargs={'pk': pk})}#comentarios")

    return redirect('noticia', noticia_id=comentario.noticia.id)

def cursos(request):
    return render(request, 'learning_logs/cursos.html')
