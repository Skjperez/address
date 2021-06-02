from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
def ListContacts(request):
    if request.user.is_authenticated is True:
        user = request.user 
    else:
        return redirect('/address/login/')
    contacts = Contact.objects.all()
    context = {
        'contactlist' : contacts
    }
    return render(request, 'contactlist/list.html', context)
    
    
    # return HttpResponse("Please enter your contact list")

def ReadContact(request, contact_id):
    try:
        contactdata = Contact.objects.get(id=contact_id)
    except Contact.DoesNotExist:
        raise Http404('Contact does not exist')
    context = {
        'contactdata': contactdata
        }
    return render(request, 'contactlist/read.html', context)


def AddContact(request):
    #check to see if user is logged in
    if request.user.is_authenticated is True:
            #if POST request we need to process the form data
        user = request.user
    else:
        return redirect('/login/')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            itemlist=Contact(
                user=user,
                contact_name=form.cleaned_data['contact_name'],
                contact_address=form.cleaned_data['contact_address'],
                contact_number=form.cleaned_data['contact_number'],
                contact_email=form.cleaned_data['contact_email'],
            )
            itemlist.save()
            # redirect to a new URL:
            return redirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        pass
    form = ContactForm()
    context = {'form':form}
    return render(request, 'contactlist/add.html', context)

            
            




