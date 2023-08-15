from django.db import models

# Create your models here.
STATUS_CHOICES = [
    ("Breakfast", "Breakfast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),
]

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image_uploads')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name} costs {self.price}"