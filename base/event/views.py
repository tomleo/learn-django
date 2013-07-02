from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from event.models import Event
from event.forms import EventForm

class detailv(DetailView):
    model = Event
    template_name = 'event/detail.html'

class listv(ListView):
    model = Event
    template_name = 'event/list.html'

class editv(UpdateView):
    model = Event
    template_name = 'event/edit.html'

class addv(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/add.html'

#def addv(request):
#
#    #event, _ = Event.objects.get_or_create(name=name, user=request.user)
#    event = Event(request.user.name)
#
#    if request.POST:
#        form = EventForm(request.POST, instance=event)
#        if form.is_valid():
#            event = form.save()
#            redirect(event)
#    else:
#        form = EventForm()
