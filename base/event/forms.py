from django.db import models
from django import forms

from event.models import Event

class CalendarWidget(forms.DateTimeInput):
    class Media:
        css = {
            
            'all': ('lib/themes/default.css',
                    'lib/themes/default.date.css',
                    'lib/themes/default.time.css',)
        }
        js = ('lib/picker.js',
              'lib/picker.date.js',
              'lib/picker.time.js',
              'lib/legacy.js',
              'django-picker.js')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time']
        widgets = {
            'date': CalendarWidget(),
            'time': CalendarWidget()
        }



