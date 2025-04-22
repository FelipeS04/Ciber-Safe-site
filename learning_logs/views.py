from django.shortcuts import render
from .models import Topic
from .models import Noticia
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework import viewsets
from .models import Topic, Entry, Noticia
from .serializers import TopicSerializer, EntrySerializer, NoticiaSerializer
from .forms import FormularioDeRegistro

# Create your views here.
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

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-date_added')
    serializer_class = TopicSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('-date_added')
    serializer_class = EntrySerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all().order_by('-data_publicacao')
    serializer_class = NoticiaSerializer
