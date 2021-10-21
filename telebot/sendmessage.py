import requests
from .models import TeleSettings


def sendTelegram(tg_m_name, tg_m_phone):
    if TeleSettings.objects.get(pk = 1):
        settings = TeleSettings.objects.get(pk = 1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat_id)
        text = str(settings.tg_message)

        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendmessage'
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            a = text.find('{')   # n{ qidiramiz tekstdagi namedan
            b = text.find('}')     # } qidiramiz tekstdagi namedan
            c = text.rfind('{')     # { qidiramiz tekstdagi phonedan
            d = text.rfind('}')     # } qidiramiz tekstdagi phonedan

            part_1  = text[0:a]      # Заявка:
            part_2 = text[b + 1:c]   # Имя: {name}
            part_3 = text[d:-1]      # Телефон: {phone}   - matndan {name} va {phone} sozlarni belgilaymiz

            text_slise = part_1 + tg_m_name + part_2 + tg_m_phone + part_3  # qolgan qismini yigib chiqamiz
        else:
            text_slise = text
        try:
            req = requests.post(method, data = {
                'chat_id': chat_id,
                'text': text_slise
                    })
        except:
            pass

        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code==500:
                print('Ошибка 500')
            else:
                print("Заявка оформлена успешно,Сообщение о заявке отправлено в телеграм канал!")
    else:
        pass




