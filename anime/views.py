import random
from django.shortcuts import render
from .models import AnimeMaterials, Index


# Create your views here.
def index(request):
    data = {'data': []}
    for i in Index.objects.all():
        data['data'].append({
            'name': i.name,
            'anime': i.anime.all(),
            'div_name': i.class_name
        })

    print(data)
    return render(request, 'anime/index.html', context=data)


def watch_anime(request, anime_slug: str):
    might_like = set()

    while len(might_like) < 4:
        might_like.add(random.randint(1, 9))

    data = {
        'anime': AnimeMaterials.objects.get(slug=anime_slug),
        'might_like': AnimeMaterials.objects.filter(pk__in=might_like)
    }
    return render(request, 'anime/anime-details.html', context=data)

