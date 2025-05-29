from django.db import models

# Create your models here.
class Topic(models.Model):
    """Um assunto sobre o qual o usuário esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação de string do modelo"""
        return self.text
    

class Entry(models.Model):
    """ALgo especifico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text[:50] + '...' if len(self.text) > 50 else self.text
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    descricao_imagem = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='noticias/', blank=True, null=True)
    conteudo = models.TextField()
    conteudo2 = models.TextField(blank=True, null=True)
    link = models.URLField(null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=100, choices=[
        ('vulnerabilidades', 'Vulnerabilidades'),
        ('ameaças', 'Ameaças'),
        ('tendencias', 'Tendências'),
        ('ciberseguranca', 'Cibersegurança'),
    ])

    def __str__(self):
        return self.titulo

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
