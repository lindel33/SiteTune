from pprint import pprint
from django.db import models
from .text_default import text_default
from .new_post import send_post
import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=4)
states = [('Отличное', 'Состояние отличное'),
          ('Хорошо', 'Состояние хорошо'),
          ('Среднее', 'Состояние Среднее'),
          ]
default_guaranty = 'Гарантия от магазина на проверку 3 месяца !✅'
default_text = text_default


class Category(models.Model):
    category = models.CharField('Категория', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.category)


class SeriesCategory(models.Model):
    category = models.CharField('Категория', max_length=100)

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

    def __str__(self):
        return str(self.category)


class Product(models.Model):
    """
    Модель товара
    """

    image_1 = models.ImageField('Картинка 1',
                                upload_to='',
                                null=False,
                                )
    image_2 = models.ImageField('Картинка 2',
                                upload_to='',
                                null=False,
                                )
    image_3 = models.ImageField('Картинка 3',
                                upload_to='',
                                null=False,
                                )
    sell = models.BooleanField('Продано?', default=False)
    price = models.SmallIntegerField('Цена')
    name = models.CharField('Название', help_text='Пример iPhone 7 128 Blue', max_length=150, null=False)
    article = models.CharField('Код товара', max_length=15, null=False)
    state = models.TextField('Состояние', choices=states, null=False)
    kit = models.CharField('Комплект', max_length=150, null=False)
    guaranty = models.CharField('Комплет', max_length=255, null=False, default=default_guaranty)

    base_text = models.TextField('Нижняя подпись к посту', null=False, default=default_text)
    day_created = models.DateTimeField('Дата создания', auto_now_add=True)
    next_edition = models.DateTimeField('Дата новой публикации', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Модель', null=True, blank=True)
    series = models.ForeignKey(SeriesCategory, on_delete=models.CASCADE,
                               verbose_name='Серия', null=True, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.sell:
            send_post([self.image_1.url,
                       self.image_2.url,
                       self.image_3.url], caption=self.text)


class ActualPrice(models.Model):
    type = models.CharField('Тип товара', max_length=100)
    price = models.TextField('Прайс')

    class Meta:
        verbose_name = 'Актуальные цены'
        verbose_name_plural = 'Актуальные цены'
