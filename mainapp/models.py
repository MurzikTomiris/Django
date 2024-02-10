from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
    name = models.CharField(
        verbose_name='Имя продукта',
        max_length=128,
    )
    image = models.ImageField(
        upload_to='product_images',
        blank=True,
        verbose_name='изображение',
    )
    short_desc = models.CharField(
        verbose_name='Краткое описание',
        max_length=100,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество товара',
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'