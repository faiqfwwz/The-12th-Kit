from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
    ('club_home', 'Club • Home'),
    ('club_away', 'Club • Away'),
    ('club_third', 'Club • Third'),
    ('club_gk', 'Club • Goalkeeper'),
    ('club_special', 'Club • Special/Anniv'),
    ('national_home', 'National • Home'),
    ('national_away', 'National • Away'),
    ('national_third', 'National • Third'),
    ('national_gk', 'National • Goalkeeper'),
    ('national_special', 'National • Special/Anniv'),
    ('retro', 'Retro/Classic'),
    ('limited', 'Limited Edition'),
    ]


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=24, choices=CATEGORY_CHOICES, default="club_home")
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, default="")
    league = models.CharField(max_length=100, blank=True, default="")
    team = models.CharField(max_length=100, blank=True, default="")
    season = models.CharField(max_length=9, blank=True, default="")