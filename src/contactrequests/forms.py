from django.forms import ModelForm
from .models import ContactReq



class ContactForm(ModelForm):
    class Meta:
        model = ContactReq
        fields = '__all__'


    
