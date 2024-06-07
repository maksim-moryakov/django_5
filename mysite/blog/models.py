from django.conf import settings
from django.db import models
from django.utils import timezone

# структура поста:

class Post(models.Model):
    # класс создан для сохранения сокращения статуса поста: опубликован или драфт
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    # поле заголовок поста, ограничение 250 символов
    title = models.CharField(max_length=250)
    # поле краткое описание постав
    slug = models.SlugField(max_length=250)
    # поле автора, модель импортирован из стандартного набора Django. поле с ключом "многие к одному" (у одного автора может быть много постов)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # при удалении пользователя, так же будет удалены все его посты
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    # поле основная часть поста
    body = models.TextField()
    # поле дата поста, по дефолту текущее время пользователя
    publish = models.DateTimeField(default=timezone.now)
    # поле дата создания поста, дата время будет сохранятся
    created = models.DateTimeField(auto_now_add=True)
    # поле храненения даты и времени обнавления поста: дата атоматически будет обновляться
    updated = models.DateTimeField(auto_now=True)
    # поле статуса поста: подефолту черновик. Тянет значения из класса Status
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    # данный класс создан для сортировки постов по полю даты создания поста
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self) -> str:
        return self.title