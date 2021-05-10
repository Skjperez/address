from django.urls import path
from .views import ContactList


urlpatterns = [
    path('contactlist/', ContactList, name='contact_list'),
    #path('', UserContactList, name='user_contact_list'),
]