import uuid
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name

class ElectricianService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='electrician_services/')

    def __str__(self):
        return self.name

class ApplianceService(models.Model):
    CATEGORY_CHOICES = [
        ('AC', 'Air Conditioner'),
        ('WM', 'Washing Machine'),
        ('RF', 'Refrigerator'),
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='appliance_services/')

    def __str__(self):
        return f"{self.get_category_display()} - {self.name}"

class PlumberService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='plumber_services/')

    def __str__(self):
        return self.name

class CarpenterService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='carpenter_services/')

    def __str__(self):
        return self.name

class PainterService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='painter_services/')

    def __str__(self):
        return self.name

class CleaningService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cleaning_services/')

    def __str__(self):
        return self.name

class SalonService(models.Model):
    GENDER_CHOICES = [
        ('Women', 'Women'),
        ('Men', 'Men'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='salon_services/')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.gender})"

class MainService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='main_services/')
    url_name = models.CharField(
        max_length=50,
        help_text="Django URL name for the detail page (e.g., 'electrician', 'appliance')"
    )

    def __str__(self):
        return self.name

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('Plumber', 'Plumber'),
        ('Electrician', 'Electrician'),
        ('Carpenter', 'Carpenter'),
        ('Mechanic', 'Mechanic'),
        ('Salon at Home', 'Salon at Home'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    description = models.TextField(blank=True)
    booking_number = models.CharField(max_length=20, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.booking_number:
            # Custom booking number: BK-YYYYMMDD-XXXX
            date_str = self.created_at.strftime('%Y%m%d') if self.created_at else ''
            unique_part = str(uuid.uuid4())[:4].upper()
            self.booking_number = f"BK-{date_str}-{unique_part}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.booking_number}"

