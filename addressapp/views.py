from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' 



#def UserContactList(request):
    #check to see if user is authenticated
    #if request.user.is_authenticated is True:
        #user = request.user
    #else user does not exist in system
    #else:
        #user = None 
    #Contact List will consist of objects that are filters under Contacts in Models.py
    #user_contact_list = Contact.objects.filter(user=user)
    #context = {
        #'contact_list' = user_contact_list,
        #'contact_form' = ContactForm()
    #}
    #return render(request, 'addressapp/address.html', context)

#def AddContact(request):
    #check if the user is logged in
    #if request.user.is_authenticated is True:
        # if this is a POST request we need to process the form data
        #if request.method == 'POST':
            # create a form instance and populate it with data from the request
            #form = ContactForm(request.POST)
            # check whether it's valid:
            #if form.is_valid():
                # process the data in form.cleaned_data as required
                #initallist = Contact(
                    #user=request.user,
                    #contact_name=form.cleaned_data['contact_name']
                #)
                #initallist.save()
                #return HttpResponseRedirect('/')


        
