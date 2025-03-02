from django.db.models.signals import post_save
from django.dispatch import receiver
from core.apps.anime.models import AnimeModel, EpisodeModel
from env import ADMIN_ID, TELEGRAM_BOT_TOKEN, BOT_URL
import requests


@receiver(post_save, sender=AnimeModel)
def generate_anime_url(sender, instance, created, **kwargs):
    if created:
        anime_url = f"{BOT_URL}?start={instance.id}"
        send_url_to_admin(anime_url)

        
        
@receiver(post_save, sender=EpisodeModel)
def generate_episode_url(sender, instance, created, **kwargs):
    if created:
        episode_url = f"Bu {instance.anime.name} qismi:\n{BOT_URL}?start={instance.id}"
        send_url_to_admin(episode_url)

        

def send_url_to_admin(url):
    admin_ids = ADMIN_ID
    message = f"{url}"
    
    telegram_bot_token = TELEGRAM_BOT_TOKEN
    send_message_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    
    for admin_id in admin_ids:
        requests.post(send_message_url, data={
            'chat_id': admin_id,
            'text': message
        })
