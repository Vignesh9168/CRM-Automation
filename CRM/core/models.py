# models.py

from django.db import models


class Agent(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    is_available = models.BooleanField(default=True)

    priority_level = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lead(models.Model):

    PRIORITY_CHOICES = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low")
    ]

    customer_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES
    )

    assigned_to = models.ForeignKey(
        Agent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    assigned_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name