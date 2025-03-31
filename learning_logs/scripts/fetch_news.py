import requests
from learning_logs.models import Noticia  # Ajuste o nome do app

API_KEY = "SUA_CHAVE_DA_API"
URL = f"https://newsapi.org/v2/top-headlines?category=technology&language=pt&apiKey={API_KEY}"

def fetch_and_save_news():
    response = requests.get(URL)
    data = response.json()

    for article in data["articles"]:
        titulo = article["title"]
        imagem_url = article["urlToImage"]
        link = article["url"]

        # Evita notícias duplicadas
        if not Noticia.objects.filter(titulo=titulo).exists():
            Noticia.objects.create(
                titulo=titulo,
                imagem=imagem_url,
                slug=titulo.lower().replace(" ", "-"),
            )
    print("Notícias atualizadas!")
