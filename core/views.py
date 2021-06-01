from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import render

from .forms import ContactForm


def index(request):
    return render(request, 'index.html')

def contact(request):
    
    form = ContactForm(request.POST or None)        


    if request.method == 'POST':
        if  form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print(f'name: {name}')
            print(f'email: {email}')
            print(f'subject: {subject}')
            print(f'message: {message}')

            messages.success(request, 'E-mail eviado com sucesso!')
            form = ContactForm()
        else:
            messages.error(request, 'erro ao enviar o email') 

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)

def product(request):
    return render(request, 'product.html')