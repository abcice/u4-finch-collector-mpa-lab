from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Chicken(models.Model):
    name = models.CharField(max_length=100, help_text='Give your chicken a ridiculous or majestic name')
    breed = models.CharField(max_length=100, help_text='e.g., Apocalypse Rooster, Galactic Hen, Drama Queen')
    description = models.TextField(max_length=250, help_text='Describe your chickens life philosophy in 250 words or less')
    age = models.IntegerField(help_text='Age of the chicken (in chicken years, or human years, who cares)')

    def __str__(self):
        return f'{self.name} the {self.breed}'

    def get_absolute_url(self):
        return reverse('chicken-detail', kwargs={'chicken_id': self.id})

class EscapeAttempt(models.Model):
    chicken = models.ForeignKey("Chicken", on_delete=models.CASCADE)
    date = models.DateTimeField("Date & time of the daring escape")
    method = models.CharField(
        max_length=100,
        help_text="How did they think this was going to work? (e.g., tunnel, fake mustache, bribery)"
    )
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.chicken.name} tried '{self.method}' on {self.date} – {'Freedom!' if self.success else 'Epic fail'}"
