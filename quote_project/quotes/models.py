from django.db import models

# Create your models here.
class QuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date_time = models.DateTimeField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    freight_type = models.CharField(max_length=50)
    pickup_address = models.TextField()
    delivery_address = models.TextField()

    def __str__(self):
        return f"QuoteRequest by {self.name} on {self.date_time}"
