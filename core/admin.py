from django.contrib import admin
from .models import LostItem

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_lost', 'status', 'reporter')
    list_filter = ('status', 'date_lost', 'location')
    search_fields = ('title', 'description', 'location', 'reporter__username')
