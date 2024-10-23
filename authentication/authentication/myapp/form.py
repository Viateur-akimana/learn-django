from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput);
    password_confirm=forms.CharField(widget=forms.PasswordInput)
    
    
    class Meta:
        model=User
        fields=["username","password","password_confirm"]
    
    def clean(self):
        cleaned_data= super().clean()
        password=cleaned_data.get("password")
        password_confirm=cleaned_data.get("password_confirm")
        
        if password and password and password != password_confirm :
            return forms.ValidationError("Passwords don't match")
        