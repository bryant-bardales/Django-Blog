from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404

from .models import ContactReq
from .forms import ContactForm

# Create your views here.


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactrequests/contactsuccess.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contactrequests/contact.html', context)

