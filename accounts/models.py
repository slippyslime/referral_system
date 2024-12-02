from django.db import models
import random
import string

def generate_invite_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, unique=True, default=generate_invite_code)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals')

    def __str__(self):
        return self.phone_number