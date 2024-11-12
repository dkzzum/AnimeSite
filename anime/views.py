import random
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import AnimeMaterials, Index, Commentaries, Category
from django.db.models import Q


# Create your views here.
def index(request: HttpRequest):
    data = {'hero': Index.objects.get(name_slug='hero')}

    for item in Index.objects.filter(~Q(name='Главное')).prefetch_related('anime__grade', 'anime__view',
                                                                          'anime__anime_commentaries', 'anime__category'):
        if item.name_slug in data.keys():
            data[item.name_slug].append(item)
        else:
            data[item.name_slug] = [item]

    return render(request, 'anime/index.html', context=data)


def watch_anime(request: HttpRequest, anime_slug: str):
    might_like = set()

    while len(might_like) < 4:
        might_like.add(random.randint(1, 9))

    anime = get_object_or_404(AnimeMaterials, slug=anime_slug)
    might_like = AnimeMaterials.objects.filter(pk__in=might_like).select_related('grade', 'view')
    commentaries = anime.anime_commentaries.all()

    data = {
        'anime': anime,
        'might_like': might_like,
        'commentaries': commentaries,
    }
    return render(request, 'anime/anime-details.html', context=data)


def page_category(request, category_slug=None, category_int=None):
    if category_slug is not None:
        print(category_slug)

    data = {
        'category': Category.objects.all()
    }

    return render(request, 'anime/categories.html', context=data)


def add_comment(request: HttpRequest, anime_slug: str):
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        anime = get_object_or_404(AnimeMaterials, slug=anime_slug)
        if comment_text:
            new_comment = Commentaries(
                user=request.user.username if request.user.is_authenticated else "Anonymous",
                commentaries=comment_text,
                anime=anime
            )
            new_comment.save()
    return redirect('watch_anime', anime_slug=anime_slug)
