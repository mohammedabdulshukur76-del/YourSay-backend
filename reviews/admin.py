from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display  = ['name', 'rating', 'type', 'is_pinned',
                     'helpful', 'created_at']
    list_filter   = ['rating', 'type', 'is_pinned']
    search_fields = ['name', 'text']
    list_editable = ['is_pinned']
    fieldsets = [
        ('Review', {
            'fields': ['name', 'location', 'type', 'rating', 'text']
        }),
        ('Status', {
            'fields': ['is_pinned', 'helpful', 'team_reply']
        }),
    ]