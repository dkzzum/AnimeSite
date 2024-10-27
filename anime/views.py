import random
from django.shortcuts import render
from .models import AnimeMaterials


# Create your views here.
def index(request):
    data = {
        'trending_now': AnimeMaterials.objects.all()[:6],
        'last_view': AnimeMaterials.objects.all()[::-1][:5],
        'hero': AnimeMaterials.objects.filter(pk__in=[3, 5, 9]),
        'last_commentaries': AnimeMaterials.objects.filter(pk__in=[4, 2, 3, 5, 1]),
    }
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

