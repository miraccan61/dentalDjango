from django.forms import ModelForm
from .models import Appointment,Contact

class AppoitmentForm(ModelForm):
    class Meta: 
        model = Appointment
        fields = ['your_name', 'your_phone', 'your_mail', 'your_address','schedule_dates','schedule_days','your_messagess']
    def __init__(self, *args, **kwargs):
        super(AppoitmentForm, self).__init__(*args, **kwargs)
        self.fields['your_name'].widget.attrs.update({'class' : 'form-control '})
        self.fields['your_phone'].widget.attrs.update({'class' : 'form-control'})
        self.fields['your_mail'].widget.attrs.update({'class' : 'form-control'})
        self.fields['your_address'].widget.attrs.update({'class' : 'form-control'})
        self.fields['schedule_dates'].widget.attrs.update({'class' : 'form-control'})
        self.fields['schedule_days'].widget.attrs.update({'class' : 'form-control'})
        self.fields['your_messagess'].widget.attrs.update({'class' : 'form-control mb-30'})

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['your_name','your_mail','your_messagess']
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['your_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['your_mail'].widget.attrs.update({'class' : 'form-control'})
        self.fields['your_messagess'].widget.attrs.update({'class' : 'form-control mb-30'})