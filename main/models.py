from django.db import models
from django.utils.text import slugify
import re

# Create your models here.
class Product(models.Model):

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

    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["slug"]),
        ]

    def _season_slug(self) -> str:
        """Ubah '2025/26' atau '25/26' jadi '25-26' untuk slug."""
        s = (self.season or "").strip()
        parts = re.findall(r"\d{2}", s)
        if len(parts) >= 2:
            return f"{parts[-2]}-{parts[-1]}"
        return s.replace("/", "-").replace(" ", "").lower()

    def _type_slug(self) -> str:
        """Ambil 'home/away/third/gk/special/retro/limited' dari category."""
        m = {
            'club_home': 'home', 'club_away': 'away', 'club_third': 'third',
            'club_gk': 'gk', 'club_special': 'special',
            'national_home': 'home', 'national_away': 'away',
            'national_third': 'third', 'national_gk': 'gk',
            'national_special': 'special',
            'retro': 'retro', 'limited': 'limited',
        }
        return m.get(self.category, 'jersey')

    def _build_slug(self) -> str:
        team = slugify(self.team or self.name or "jersey")
        season = self._season_slug()
        t = self._type_slug()
        # format akhir: liverpool-fc-25-26-third-jersey
        base = f"{team}"
        if season:
            base += f"-{season}"
        if t:
            base += f"-{t}"
        base += "-jersey"
        return base

    def save(self, *args, **kwargs):
        # generate slug kalau kosong / berubah data kunci
        if not self.slug:
            candidate = self._build_slug()
            unique = candidate
            i = 2
            while Product.objects.filter(slug=unique).exclude(pk=self.pk).exists():
                unique = f"{candidate}-{i}"
                i += 1
            self.slug = unique
        super().save(*args, **kwargs)

class Employee(models.Model):
    name = models.CharField(max_length=255)#maks 255 
    age = models.IntegerField() #bil bulat
    persona = models.TextField() #description