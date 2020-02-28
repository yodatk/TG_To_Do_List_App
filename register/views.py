# views.py
from django.shortcuts import render
from .forms import RegisterForms
from django.http import HttpResponseRedirect


# Create your views here.
def register(request):
    """
    registering the new user if possible.
    if not -> will remain in registration page , and show the errors in registration forms.
    otherwise, will register the new user and return to home page
    :param request:  http request
    :return: Registration page html if form was valid, other wise -> go back to home page
    """
    if request.method == "POST":
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegisterForms()

    return render(request, "register/register.html", {"form": form})
