from django.urls import path
from .views import contact_page,contact_success_page,home_page


urlpatterns=[
    path('',home_page,name='home'),
    path('contact/',contact_page,name="contact"),
    path('contact/success/',contact_success_page,name='contact_success')
    
]