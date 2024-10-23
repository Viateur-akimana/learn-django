from django.urls import path
from .views import login_view, logout_view, register_view, home_view, ProtectedView

urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/register/', register_view, name='register'),
    path('registration/protected/', ProtectedView.as_view(), name='protected'),
]
