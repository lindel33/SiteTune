
from django.db import models
from .text_default import text_default


class Category(models.Model):
    category = models.CharField('Категория', max_length=100)

    def __str__(self):
        return str(self.category)

class Product(models.Model):
    """
    Модель товара
    """

    image_1 = models.ImageField('Картинка 1', upload_to='media', null=False, default='default.jpg')
    image_2 = models.ImageField('Картинка 2', upload_to='media', null=False, default='default.jpg')
    image_3 = models.ImageField('Картинка 3', upload_to='media', null=False, default='default.jpg')
    image_4 = models.ImageField('Картинка 4', upload_to='media', null=True, blank=True, default='default.jpg')
    image_5 = models.ImageField('Картинка 5', upload_to='media', null=True, blank=True, default='default.jpg')

    name = models.CharField('Название', max_length=100, null=False)
    article = models.CharField('Артикул', max_length=50, null=False)
    text = models.TextField('Описание', max_length=5000, null=False, default=text_default)
    sell = models.BooleanField('Продано', default=False)

    day_created = models.DateTimeField('Дата создания', auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'




