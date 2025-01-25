from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import JsonResponse

def index(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            send_mail(
                f"Message de {name}",
                message,
                email,
                ['masanenoyume@gmail.com'],
                fail_silently=False,
            )
            success=True
            failure=False
        else:
            success=False
            failure=True
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
        success=False
        failure=True

    return render(request, "index.html", {"form": form,"success":success,"failure":failure})

