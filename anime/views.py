import random
from django.shortcuts import render, get_object_or_404
from .models import AnimeMaterials, Index, Commentaries
from django.db.models import Q


# Create your views here.
def index(request):
    data = {'hero': Index.objects.get(name_slug='hero')}

    for item in Index.objects.filter(~Q(name='Главное')):
        if item.name_slug in data.keys():
            data[item.name_slug].append(item)
        else:
            data[item.name_slug] = [item]

    return render(request, 'anime/index.html', context=data)


def watch_anime(request, anime_slug: str):
    might_like = set()

    while len(might_like) < 4:
        might_like.add(random.randint(1, 9))

    anime = get_object_or_404(AnimeMaterials, slug=anime_slug)
    data = {
        'anime': anime,
        'might_like': AnimeMaterials.objects.filter(pk__in=might_like),
        'commentaries': anime.anime_commentaries.all()
    }
    return render(request, 'anime/anime-details.html', context=data)

