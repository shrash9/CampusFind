from django.db import models
from django.contrib.auth.models import User

class LostItem(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('claimed', 'Claimed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_lost = models.DateField()
    photo = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lost_items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
