from django.db import models

class Type(models.Model):
    type_name = models.CharField(max_length=50)
    type_img = models.ImageField(null=True, blank=True)

    def __str__(self):  # как будет передаваться название
        return self.type_name

    class Meta:
        verbose_name_plural = 'Типы блюда'
        verbose_name = 'Тип блюда'

class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    picture = models.ImageField(null=True, blank=True)
    discription = models.TextField()
    price = models.IntegerField(null=True)
    type_name = models.ForeignKey(Type, on_delete = models.PROTECT, null=True)

    def __str__(self):  # как будет передаваться название
        return self.name

    class Meta:
        verbose_name_plural = 'Позиции меню'
        verbose_name = 'Позиция меню'


class Reservation(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    date = models.DateField(verbose_name='Дата')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')

    def __str__(self):  # как будет передаваться название
        return self.name

    class Meta:
        verbose_name_plural = 'Бронь'
        verbose_name = 'Бронь'


