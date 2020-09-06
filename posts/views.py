"""Posts views. """

#Django
from django.shortcuts import render

#Utilidades
from django.http import HttpResponse
from datetime import datetime

posts =[
    {
        'name': 'Mont Blac',
        'user': 'Melissa Tirado',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Láctea',
        'user': 'Miguel Valdez',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Raquel Reynoso',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1076',
    },
]

# Create your views here.
def list_posts(request):
    """Lista de posts existentes."""
    content = []
    for post in posts:
            content.append("""
                <p><strong>{name}</strong></p>
                <p><small>{user} - <i>{timestamp}</i></small></p>
                <figure><img src="{picture}"/></figure>
            """.format(**post))
    return HttpResponse('<br>'.join(content))