# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.apps.anime.models import AnimeModel
from env import ADMIN_ID, TELEGRAM_BOT_TOKEN, BOT_URL
import requests


@receiver(post_save, sender=AnimeModel)
def generate_anime_url(sender, instance, created, **kwargs):
    if created:
        unique_id = f"anime_{instance.id}"
        anime_url = f"{BOT_URL}?start={unique_id}"
        
        send_url_to_admin(anime_url)


def send_url_to_admin(url):
    admin_id = ADMIN_ID
    message = f"{url}"
    
    telegram_bot_token = TELEGRAM_BOT_TOKEN
    send_message_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    
    requests.post(send_message_url, data={
        'chat_id': admin_id,
        'text': message
    })
