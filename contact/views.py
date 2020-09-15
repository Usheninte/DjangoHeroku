from django.views.generic.edit import CreateView

from .forms import ContactForm
from .models import ContactInfo


class ContactView(CreateView):
    model = ContactInfo
    form_class = ContactForm
    template_name = 'main.html'
