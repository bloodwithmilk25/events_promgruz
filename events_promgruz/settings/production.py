from .local import *

with open('/etc/events_promgruz') as f:
    SECRET_KEY = f.read().strip()

GOOGLE_MAPS_API_KEY = 'AIzaSyAlhlthQomcbCaSMrnBflTd4dROwCRewn8'

DEBUG = False

ALLOWED_HOSTS = ['events.mitenka.dp.ua', 'event.promgruz.com', 'events.promgruz.com']
