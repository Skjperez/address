from django.urls import path
from .views import ContactList, AddContact


urlpatterns = [
    #path('contactlist/', ContactList, name='contact_list'),
    #path('', UserContactList, name='user_contact_list'),
    path('add/', AddContact, name='add')
]