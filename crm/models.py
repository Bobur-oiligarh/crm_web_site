from django.db import models

class StatusCrm(models.Model):
    status_name = models.CharField(max_length = 200, verbose_name='Название cтатуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now = True)
    order_name = models.CharField(max_length= 200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Тел')
    order_status = models.ForeignKey(StatusCrm, on_delete = models.PROTECT, null = True, blank = True, verbose_name = 'Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete = models.CASCADE, verbose_name = "Заявка")
    coment_text = models.TextField(verbose_name = "Текс комментария")
    coment_dt = models.DateTimeField(auto_now = True, verbose_name = "Дата создания")

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"