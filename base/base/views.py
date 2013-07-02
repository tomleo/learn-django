from django.core.urlresolvers import reverse
#from django.views.generic import RedirectView
from django.views.generic import TemplateView

class home(TemplateView):
    #url = reverse('event-list')
    template_name = 'home.html'
