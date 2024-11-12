from django.db import models
from django.db.models import F, Value
from django.urls import reverse


class AnimeTitlesManager(models.Manager):
    def by_date_added(self, descending=True):
        # Фильтрация по дате добавления с сортировкой по убыванию или возрастанию
        ordering = '-date_add' if descending else 'date_add'
        return self.order_by(ordering)

    def by_grade(self, descending=True):
        # Фильтрация по рейтингу с сортировкой
        ordering = '-grade' if descending else 'grade'
        return self.order_by(ordering)

    def by_views(self, descending=True):
        # Фильтрация по числу просмотров с сортировкой
        ordering = '-views' if descending else 'views'
        return self.order_by(ordering)


class AnimeMaterials(models.Model):
    class Status(models.TextChoices):
        IS_OUT = 'Вышел', 'Is out'
        ONGOING = 'Онгоинг', 'Ongoing'

    class Rating(models.TextChoices):
        GENERAL_AUDIENCE = 'G', 'Подходит для всех возрастов.'
        PARENTAL_GUIDANCE = 'PG', 'Рекомендуется просмотр в присутствии родителей.'
        PARENTS_STRONGLY_CAUTIONED = 'PG-13', 'Рекомендуется для подростков 13 лет и старше.'
        RESTRICTED = 'R', 'Подходит для лиц старше 17 лет.'
        MILD_NUDITY = 'R+', 'Содержит легкую наготу или более откровенные сцены.'

    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    en_title = models.CharField(blank=True, max_length=255)
    jp_title = models.CharField(blank=True, max_length=255)
    episode = models.IntegerField(blank=True, default=12)
    status = models.TextField(choices=Status, default=Status.IS_OUT)
    description = models.TextField(blank=True)
    date_create = models.DateField(blank=True, auto_now_add=True)
    date_add = models.DateField(auto_now_add=True)
    rating = models.TextField(choices=Rating, default=Rating.GENERAL_AUDIENCE)

    studio = models.ForeignKey(to='Studio', null=True, on_delete=models.PROTECT, related_name='studio')
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


class Commentaries(models.Model):
    class Meta:
        ordering = ['-data_create']

    user = models.CharField(max_length=255)
    commentaries = models.TextField(max_length=10000)
    data_create = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    anime = models.ForeignKey(to='AnimeMaterials', on_delete=models.SET_NULL, blank=True, null=True,
                              related_name='anime_commentaries')


class Studio(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Index(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField(max_length=255, blank=True, null=True, unique=False)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    anime = models.ManyToManyField(to='AnimeMaterials', blank=True, related_name='anime')


class Views(models.Model):
    view = models.IntegerField(default=0, blank=True)
    unique_views = models.IntegerField(default=0, blank=True)

    def add_view(self):
        self.view = F('view') + 1
        self.save(update_fields=['view'])

        self.refresh_from_db()
        return f'{self.view}'

    def __str__(self):
        return str(self.view)


class Grade(models.Model):
    grade = models.DecimalField(default=0, blank=True, max_digits=10, decimal_places=1)
    sum = models.IntegerField(null=True, blank=True, default=0)
    quantity = models.IntegerField(default=0, blank=True)

    def set_grade(self, new_grade):
        self.sum = F('sum') + new_grade
        self.quantity = F('quantity') + 1
        self.save()

    def calculation_grade(self):
        self.grade = F('sum') / F('quantity')
        self.save()

    def show_grade(self):
        return str(self.grade)[:4]

    def __str__(self):
        if self.grade != 0 and self.quantity >= 100:
            return f'{str(self.grade)[:4]} / 10'
        else:
            return '? / 10'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name
