from django.db import models

# Create your models here.

class ContactForm(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    drzava= models.CharField(max_length=100)
    subjekt = models.CharField(max_length=100)


class StartingPage(models.Model):
    template_name = "my_shop/index.html"