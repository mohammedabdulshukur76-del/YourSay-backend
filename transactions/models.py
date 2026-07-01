from django.db import models

class Transaction(models.Model):

    TYPE_CHOICES = [
        ('credit', 'Credit (In)'),
        ('debit',  'Debit (Out)'),
    ]

    STATUS_CHOICES = [
        ('received',  'Received'),
        ('completed', 'Completed'),
        ('progress',  'In Progress'),
        ('voting',    'Voting'),
    ]

    CATEGORY_CHOICES = [
        ('government',   'Government'),
        ('donation',     'Donation'),
        ('corporate',    'Corporate'),
        ('healthcare',   'Healthcare'),
        ('education',    'Education'),
        ('infrastructure','Infrastructure'),
        ('disaster',     'Disaster Relief'),
        ('other',        'Other'),
    ]

    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)
    amount      = models.DecimalField(max_digits=12, decimal_places=2)
    type        = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category    = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES)
    icon        = models.CharField(max_length=10, default='📋')
    date        = models.DateField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — ₹{self.amount}"

    class Meta:
        ordering = ['-date', '-created_at']