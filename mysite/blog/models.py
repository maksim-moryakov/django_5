from django.db import models

# структура поста: заголовок (250 символов); краткое описание (250 символов); основной текст

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title