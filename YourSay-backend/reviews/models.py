from django.db import models

class Review(models.Model):

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    TYPE_CHOICES = [
        ('ui',          'UI / Design'),
        ('feature',     'Feature Request'),
        ('bug',         'Bug Report'),
        ('content',     'Content Feedback'),
        ('general',     'General Review'),
    ]

    name       = models.CharField(max_length=100)
    location   = models.CharField(max_length=100, blank=True)
    type       = models.CharField(max_length=20, choices=TYPE_CHOICES,
                                  default='general')
    rating     = models.IntegerField(choices=RATING_CHOICES, default=5)
    text       = models.TextField()
    helpful    = models.IntegerField(default=0)
    is_pinned  = models.BooleanField(default=False)
    team_reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} — {self.rating}★'

    class Meta:
        ordering = ['-is_pinned', '-created_at']