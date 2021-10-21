from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm


class Coment(admin.StackedInline):
    model = ComentCrm                        # наследование коментов
    fields = ('coment_dt', 'coment_text')    # показ выделенных полей
    readonly_fields = ('coment_dt',)                # поля только для чтения
    extra = 0                                # оставить 1 экземпляр подкласса комент (в дефолт выводится 3экзмплр)




class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')   # Вывод соответ выделенных переменных
    list_display_links = ('id', 'order_name')                                        # столбцы, кликаемые (ссылки)
    search_fields = ('id', 'order_status', 'order_name', 'order_phone',)             # Поля по которым будет производить поиск
    list_filter = ('order_status',)                                               # выбор столбцов для фильтра справа экрана
    list_editable = ('order_status',  'order_phone')                      #  поля которых можно изменять на данной же странице
    list_per_page = 10                                         # количество записей которых надо показать в странице
    list_max_show_all = 100             # Колич записей которых надо показать при нажатии "показать все"
    fields = ('id', 'order_status', 'order_dt','order_name', 'order_phone')  # поля которыъх нужно показать внутри каждой записи
    readonly_fields = ('id', 'order_dt')      # поля которые определены только для чтения

    inlines = [Coment]                 # показать обьект класса комент внутри класса ордер

admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)