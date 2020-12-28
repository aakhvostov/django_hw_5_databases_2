from django.db import models


# класс статьи
class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scopes = models.ManyToManyField('Scope', blank=True, related_name='articles', through='ScopeToArticle')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


# класс тегов
class Scope(models.Model):
    topic = models.CharField(max_length=30, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.id} - {self.topic}'


# промежуточный класс связи статей и тегов
class ScopeToArticle(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='article_topic')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='topic_article')
    is_main = models.BooleanField(verbose_name='Основной раздел')

    def __str__(self):
        return f"{self.scope} - {self.article}"
