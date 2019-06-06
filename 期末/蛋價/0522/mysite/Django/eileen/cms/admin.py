from django.contrib import admin
from .models import egg
# Register your models here.

class eggAdmin(admin.ModelAdmin):
	list_display = ('kind', 'price', 'region')

admin.site.register(egg)