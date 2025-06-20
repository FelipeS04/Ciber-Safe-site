"""
URL configuration for learnig_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticia/<int:pk>/', views.noticia, name='noticia'),
    path('noticia/<int:pk>/comentario/<int:comentario_id>/excluir/', views.excluir_comentario, name='excluir_comentario'),
    path('noticia/<int:pk>/comentario/<int:comentario_id>/editar/', views.editar_comentario, name='editar_comentario'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('servico/', views.servico, name='erro'),
    path('topics/', views.topics, name='topics'),
    path('criar-conta/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='learning_logs/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/', include('learning_logs.api_urls')),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/curso_01/', views.curso_01, name='curso_01'),
    path('cursos/', views.cursos, name='cursos'),
]
