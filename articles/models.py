from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tag(models.Model):

    title = models.CharField(max_length=256, verbose_name='Tags')

    def __str__(self):
        return self.title


class Scope(models.Model):

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tag')