from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    groups = models.ManyToManyField(
    'auth.Group',
    related_name='guessr_user_set',  # Custom related_name to avoid conflict
    blank=True,
    help_text='The groups this user belongs to.',
    verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
    'auth.Permission',
    related_name='guessr_user_set',  # Custom related_name to avoid conflict
    blank=True,
    help_text='Specific permissions for this user.',
    verbose_name='user permissions'
    )

class Player(models.Model):
    name = models.CharField(max_length=32)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, related_name='player', null=True)
    nation = models.CharField(max_length=32)
    role = models.CharField(max_length=32)
    role2 = models.CharField(max_length=32, null=True, default='null')
    age = models.IntegerField()
    image = models.TextField(null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, related_name='players', null=True)
    def __str__(self):
        return f"{self.name}"

class Region(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    name = models.CharField(max_length=32)
    image = models.TextField(null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, related_name='teams', null=True)
    top30 = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='stat')
    rating = models.FloatField()
    majorApps = models.IntegerField()
    majorWin = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player}"
    
class PlayerAttributes(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='attributes')
    firepower = models.IntegerField(default=0)
    entrying = models.IntegerField(default=0)
    trading = models.IntegerField(default=0)
    opening = models.IntegerField(default=0)
    clutching = models.IntegerField(default=0)
    sniping = models.IntegerField(default=0)
    utility = models.IntegerField(default=0)

class UserStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pstats')
    day = models.ForeignKey('DailyPlayer', on_delete=models.CASCADE, related_name='completed')
    guesses = models.IntegerField(default=6)
    def __str__(self):
        return f"{self.user}"
    
class DailyPlayer(models.Model):
    date = models.DateField(unique=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.date}: {self.player}"