from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from threading import Timer
from main.models import Event
import datetime


def start():
    tomorrow = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), datetime.time.min)
    timedelta = tomorrow - datetime.datetime.now()
    timer = Timer(timedelta.seconds, notify)
    timer.start()


def notify():
    today = timezone.make_aware(datetime.datetime.today())
    users = User.objects.all()
    for user in users:
        events = Event.objects.filter(user=user).filter(start_date_time__date=today)
        if events.exists():
            send_mail('Wydarzenia {}'.format(today.strftime('%Y-%m-%d')), format_events(events), 'admin', [user.email])
    start()


def format_events(events):
    info = []
    for event in events:
        info.append('{}, {}, {}-{}'.format(event.name, event.description,
                                           event.start_date_time.astimezone().strftime('%H:%M'),
                                           event.end_date_time.astimezone().strftime('%H:%M')))
    return '\n'.join(info)
