from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse 
from django.http import HttpResponseRedirect

# Create your views here.
def ContactList(request):
    if request.user.is_authenticated is True:
        user = request.user 
    else:
        return redirect('/address/login/')
    return HttpResponse("Please enter your contact list")

    #filtering the objects listed under Contacts in model
    #user_contact_list = Contact.objects.filter(user=user)
    #context = {
        #'contact_list' : user_contact_list,
        #'contact_form' : ContactForm()
    #}
    #return render(request,'contactlist.html',context)

def AddContact(request):
        #check to see if user is logged in
    if request.user.is_authenticated is True:
            #if POST request we need to process the form data
        user = request.user
    else:
        return redirect('/login/')
    
    if request.method == 'POST':
            #A form associated with the POST data
        form = ContactForm(request.POST)
            #to determine if the form is valid
        if form.is_valid():
                #process the data inside the form
            itemlist=Contact(
                user=user,
                contact_name=form.cleaned_data['contact_name'],
                contact_address=form.cleaned_data['contact_address'],
                contact_number=form.cleaned_data['contact_name'],
                contact_email=form.cleaned_data['contact_email'],
            )
            itemlist.save()
            return redirect('home')
    else:
        return render(request,'add.html')




