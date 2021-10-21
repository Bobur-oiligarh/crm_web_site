from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram


def first_page(request):
    price_1 = PriceCard.objects.get(pk=1)
    price_2 = PriceCard.objects.get(pk=2)
    price_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    slaider_list = CmsSlider.objects.all()
    form = OrderForm()
    content = {'price_1': price_1,
               'price_2': price_2,
               'price_3': price_3,
               'price_table': price_table,
               'slaider_list': slaider_list,
               'form': form}
    return render(request, './index.html', content)


def thanks_page(request):
     if request.POST:
        name = request.POST['name']
        phone_number = request.POST['phone']
        element = Order(order_name=name, order_phone=phone_number)
        element.save()
        sendTelegram(tg_m_name = name, tg_m_phone = phone_number)
        return render(request, 'thanks.html', {'name': name,
                                               'phone': phone_number})
     else:
        return render(request, 'thanks.html')
