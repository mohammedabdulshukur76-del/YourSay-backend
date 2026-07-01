from django.db import models

class Issue(models.Model):

    STATUS_CHOICES = [
        ('open',     'Open'),
        ('review',   'Under Review'),
        ('funded',   'Funded'),
        ('progress', 'In Progress'),
        ('done',     'Completed'),
        ('urgent',   'Urgent'),
    ]

    CATEGORY_CHOICES = [
        ('healthcare',     'Healthcare'),
        ('education',      'Education'),
        ('infrastructure', 'Infrastructure'),
        ('water',          'Water & Sanitation'),
        ('safety',         'Safety'),
        ('environment',    'Environment'),
        ('disaster',       'Disaster Relief'),
        ('other',          'Other'),
    ]

    title       = models.CharField(max_length=200)
    description = models.TextField()
    location    = models.CharField(max_length=150)
    category    = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    fund_goal   = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fund_raised = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    votes       = models.IntegerField(default=0)
    submitted_by= models.CharField(max_length=100, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-votes', '-created_at']