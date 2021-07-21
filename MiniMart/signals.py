from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def make_profile(sender , instance, created, **kwargs):
    if created:
        group = Group.objects.get(name = "customer")
        instance.groups.add(group)
        Customer.objects.create(
                user=instance,
                name = instance.username,
                    )
post_save.connect(make_profile, sender = User)