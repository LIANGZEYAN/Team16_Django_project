from django.db import models
from django.template.defaultfilters import slugify


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    publisher = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=128)
    poster = models.ImageField()
    store_link = models.URLField()
    avg_quality_rate = models.FloatField(default=0.0)
    avg_music_rate = models.FloatField(default=0.0)
    avg_community_rate = models.FloatField(default=0.0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    quality_rate = models.IntegerField(default=0)
    music_rate = models.IntegerField(default=0)
    community_rate = models.IntegerField(default=0)

    def __str__(self):
        return self.content
