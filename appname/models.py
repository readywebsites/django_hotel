from django.db import models

# Example Model
class Item(models.Model):
    name = models.CharField(max_length=200)  # Name of the item
    description = models.TextField(blank=True, null=True)  # Optional description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return self.name  # String representation for the admin panel
