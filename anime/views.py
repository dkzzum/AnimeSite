import random
from django.shortcuts import render
from .models import AnimeMaterials, Index
from django.db.models import Q


# Create your views here.
def index(request):
    data = {'hero': Index.objects.get(nslug='hero')}

    for item in Index.objects.filter(~Q(name='Главное')):
        if item.nslug in data.keys():
            data[item.nslug].append(item)
        else:
            data[item.nslug] = [item]

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

