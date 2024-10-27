from django.db import models
from django.urls import reverse


class AnimeTitlesManager(models.Manager):
    def by_date_added(self, descending=True):
        # Фильтрация по дате добавления с сортировкой по убыванию или возрастанию
        ordering = '-date_add' if descending else 'date_add'
        return self.order_by(ordering)

    def by_grade(self, descending=True):
        # Фильтрация по рейтингу с сортировкой
        ordering = 'grade' if descending else '-grade'

    def by_views(self, descending=True):
        # Фильтрация по числу просмотров с сортировкой
        ordering = '-views' if descending else 'views'
        return self.order_by(ordering)


# add manager
class AnimeMaterials(models.Model):
    class Status(models.TextChoices):
        IS_OUT = 'Вышел', 'Is out'
        ONGOING = 'Онгоинг', 'Ongoing'

    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    en_title = models.CharField(blank=True, max_length=255)
    jp_title = models.CharField(blank=True, max_length=255)
    # episode = models.IntegerField(blank=True, default=12)
    status = models.TextField(choices=Status, default=Status.IS_OUT)
    studio = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    commentaries = models.IntegerField(default=0, blank=True)
    date_create = models.DateField(blank=True, auto_now_add=True)
    date_add = models.DateField(auto_now_add=True)
    view = models.OneToOneField(to='Views', blank=True, null=True, on_delete=models.PROTECT, related_name='views')
    category = models.ManyToManyField(to='Category', blank=True, related_name='category')
    grade = models.OneToOneField(to='Grade', blank=True, null=True, on_delete=models.SET_NULL, related_name='grades')
    img = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('watch_anime', kwargs={'anime_slug': self.slug})

    animanager = AnimeTitlesManager()
    objects = models.Manager()


class Views(models.Model):
    view = models.IntegerField(default=0, blank=True)
    unique_views = models.IntegerField(default=0, blank=True)

    def add_view(self):
        self.view += 1
        self.save()

    def __str__(self):
        return str(self.view)


class Grade(models.Model):
    grade = models.DecimalField(default=0, blank=True, max_digits=10, decimal_places=1)
    sum = models.IntegerField(null=True, blank=True, default=0)
    quantity = models.IntegerField(default=0, blank=True)

    def __str__(self):
        if self.grade != 0 and self.quantity >= 100:
            return f'{self.grade} / 10'
        else:
            return '? / 10'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name
