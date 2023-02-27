from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    title = models.CharField(
        verbose_name='Заголовок задачи',
        max_length=70,
        )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        max_length=300,
        )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
        )

    deadline = models.DateTimeField(
        blank=True,
        verbose_name='Крайний срок',)

    is_done = models.BooleanField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
