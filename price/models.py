from django.db import models

class PriceCard(models.Model):
    pricecard_value = models.CharField( max_length = 20, verbose_name = 'Цена')
    pricecard_discription = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.pricecard_value

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"


class PriceTable(models.Model):
    pricetable_title = models.CharField( max_length = 200, verbose_name = 'Услуги')
    pricetable_old_price = models.CharField(max_length=20, verbose_name='Старая цена')
    pricetable_new_price = models.CharField(max_length=20, verbose_name='Новая цена')

    def __str__(self):
        return self.pricetable_title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"










