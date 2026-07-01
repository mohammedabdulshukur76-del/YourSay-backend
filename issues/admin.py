from django.contrib import admin
from .models import Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):

    list_display = [
        'title', 'category', 'status',
        'votes', 'fund_goal', 'fund_raised',
        'location', 'created_at'
    ]

    list_filter = ['status', 'category']

    search_fields = ['title', 'location', 'submitted_by']

    list_editable = ['status']

    fieldsets = [
        ('Issue Details', {
            'fields': ['title', 'description', 'location',
                       'category', 'status', 'submitted_by']
        }),
        ('Funding', {
            'fields': ['fund_goal', 'fund_raised']
        }),
        ('Engagement', {
            'fields': ['votes']
        }),
    ]