from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.

# Page for homepage
def home_page(request):
    return render(request, 'pages/home.html')

# Page for contact form
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email() 
            return redirect('contact_success')  
    else:
        form = ContactForm()  

    return render(request, 'pages/contact.html', {"form": form})  

# Page for success 
def contact_success_page(request):
    return render(request, "pages/contact_success.html")  
