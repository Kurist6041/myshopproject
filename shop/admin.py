from django.contrib import admin
from .models import ItemPost

class ItemPostAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'user', 'image', 'name', 'description','price')
    
    list_display_links = ('id', 'user', 'image', 'name', 'description','price')

admin.site.register(ItemPost, ItemPostAdmin)
