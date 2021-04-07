from pupa.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    # отправка уведомления по электронной почте при успешном создании заказа
    # send email notification when order is successfully created
    order = Order.objects.get(id=order_id)
    subject = 'Заказ №. {}'.format(order_id)
    message = 'Привет {0} (◕‿◕),\n\n\
    Рад сообщить тебе, что твой заказ под номером {1}\n\
    был успешно оформлен! ٩(◕‿◕)۶\n\n\
    Спасибо тебе (◕‿◕)♡,\n\
    С уважением yamitoys!'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'yamitoys@gmail.com',
                          [order.email])
    return mail_sent
