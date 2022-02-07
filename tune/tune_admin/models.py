from django.db import models
from .text_default import text_default
from .new_post import send_post
import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=4)


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
                                upload_to='media',
                                null=False,
                                default='default.jpg')
    image_2 = models.ImageField('Картинка 2',
                                upload_to='media',
                                null=False,
                                default='default.jpg')
    image_3 = models.ImageField('Картинка 3',
                                upload_to='media',
                                null=False,
                                default='default.jpg')
    image_4 = models.ImageField('Картинка 4',
                                upload_to='media',
                                null=True,
                                blank=True,
                                default='default.jpg')
    image_5 = models.ImageField('Картинка 5',
                                upload_to='media',
                                null=True,
                                blank=True,
                                default='default.jpg')

    name = models.CharField('Название', max_length=100, null=False)
    article = models.CharField('Артикул', max_length=50, null=False)
    text = models.TextField('Описание', max_length=5000, null=False, default=text_default)
    sell = models.BooleanField('Продано', default=False)

    day_created = models.DateTimeField('Дата создания', auto_now_add=True)
    next_edition = models.DateTimeField('Дата новой публикации', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    series = models.ForeignKey(SeriesCategory, on_delete=models.CASCADE,
                               verbose_name='Серия', null=True, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def save(self, *args, **kwargs):
        if not self.sell:
            send_post([self.image_1.path,
                       self.image_2.path,
                       self.image_3.path], caption=self.text)
        super().save(*args, **kwargs)
