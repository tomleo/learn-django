from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def get_absolute_url(self):
        return reverse('event-detail', args=(self.id,))
