from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Player)
admin.site.register(Region)
admin.site.register(Team)
admin.site.register(PlayerStats)
admin.site.register(PlayerAttributes)
admin.site.register(UserStats)
admin.site.register(DailyPlayer)