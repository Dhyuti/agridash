import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Plant

@receiver(post_delete, sender=Plant)
def delete_plant_media(sender, instance, **kwargs):
    # Check if there is an image and if the file exists
    if instance.image:
        file_path = instance.image.path
        if os.path.isfile(file_path):
            os.remove(file_path)
