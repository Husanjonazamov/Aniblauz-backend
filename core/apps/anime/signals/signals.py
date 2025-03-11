from django.db.models.signals import post_save
from django.dispatch import receiver
from core.apps.anime.models import AnimeModel, EpisodeModel
from env import ADMIN_ID, TELEGRAM_BOT_TOKEN, BOT_URL
import requests


@receiver(post_save, sender=AnimeModel)
def generate_anime_url(sender, instance, created, **kwargs):
    if created:
        anime_url = f"{str(instance.name)}\n{str(BOT_URL)}?start={str(instance.id)}"

        url = anime_url.split(f"{str(instance.name)}")[1]
        instance.link = url
        instance.save()
        instance._meta.get_field('link').editable = True
        
        send_url_to_admin(anime_url)
        
        
@receiver(post_save, sender=EpisodeModel)
def generate_episode_url(sender, instance, created, **kwargs):
    if created:
        episode_url = f"{str(instance.name)}\n{str(BOT_URL)}?start={str(instance.id)}"
        
        url = episode_url.split(f"{str(instance.name)}")[1]
        instance.link = url
        instance.save()
        instance._meta.get_field('link').editable = True
        send_url_to_admin(episode_url)
        

def send_url_to_admin(url):
    admin_ids = [5765144405,5303925509]
    message = f"{url}"
    
    telegram_bot_token = TELEGRAM_BOT_TOKEN
    send_message_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    
    if isinstance(admin_ids, list):
        for admin_id in admin_ids:
            try:
                response = requests.post(send_message_url, data={
                    'chat_id': admin_id,
                    'text': message,
                    'parse_mode': 'HTML'
                })
                response.raise_for_status()  
            except requests.exceptions.RequestException as e:
                print(f"Error sending message to admin {admin_id}: {e}")
