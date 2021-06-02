from django.urls import path
from .views import ListContacts, AddContact, ReadContact


urlpatterns = [
    path('', ListContacts, name='list_contacts'),
    path('add/', AddContact, name='add_contact'),
    path('<int:contact_id>/', ReadContact, name='read_contact'),
    #path('<int:id>/update/', UpdateContact, name='update_contact'),
    #path('<int:id>/delete/', DeleteContact, name='delete_contact')

]