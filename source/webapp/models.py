from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    poll = models.ForeignKey('webapp.Choice', related_name='polls_choice',
                             on_delete=models.PROTECT, null=False, blank=False, verbose_name='варианты')


class Choice(models.Model):
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    poll = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')