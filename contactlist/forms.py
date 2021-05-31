from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Contact Name',max_length=50)
    contact_address = forms.CharField(label='Contact Address',max_length=100)
    contact_number = forms.CharField(label='Contact Number',max_length=15)
    contact_email = forms.EmailField(label='Contact Email',max_length=50)
