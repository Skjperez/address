from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect
from .models import Contact
#from .forms import ContactForm
from django.http import HttpResponse 

# Create your views here.
def ContactList(request):
    return HttpResponse("Please enter your contact list")

#make sure the user is authenticated when accessing their contact list
#def UserContactList(request):
    #if request.user.is_authenticated is True:
        #user = request.user 
    #else:
        #return redirect('/address/login/')
    #filtering the objects listed under Contacts in model
    #user_contact_list = Contact.objects.filter(user=user)
    #context = {
        #'contact_list' : user_contact_list,
        #'contact_form' : ContactForm()
    #}
    #return render(request,'contactlist.html',context)



