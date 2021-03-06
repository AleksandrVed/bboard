from django.db import models
from django.contrib.auth.models import User

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null = True, on_delete=models.PROTECT, verbose_name='Рубрика')
    author = models.ForeignKey(User, null = True, blank=True, on_delete=models.CASCADE, verbose_name='Автор')
    class Meta:
        verbose_name_plural='Объявления'
        verbose_name='Объявление'
        ordering = ['-published']
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name