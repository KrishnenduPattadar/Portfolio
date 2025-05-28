from django.db import models

# Create your models here.
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Inquiry from {self.name} ({self.email})"
    
    class Meta:
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"