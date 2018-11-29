from django.contrib import admin
from .models import Favourite, Comments

# Register your models here.
admin.site.register(Favourite),
admin.site.register(Comments)
