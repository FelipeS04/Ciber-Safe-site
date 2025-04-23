from rest_framework import serializers
from .models import Topic, Entry, Noticia

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'text', 'date_added']
        read_only_fields = ['date_added']

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'topic', 'text', 'date_added']
        read_only_fields = ['date_added']

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'conteudo', 'data_publicacao', 'categoria']
        read_only_fields = ['data_publicacao']
