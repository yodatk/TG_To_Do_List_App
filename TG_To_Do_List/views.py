from django.shortcuts import render, redirect
from django.utils import timezone
from TG_To_Do_List import models
from django.http import HttpResponseRedirect
from register.forms import RegisterForms



# # Create your views here.
# def home(request):
#     # """
#     # rendering the home page
#     # :param request: Request param
#     # :return: rendered page of the home page
#     # """
#     # # todo_items = models.Todo.objects.all().order_by("-added_date")
#     # return render(request, 'main/register.html')  # , {
#     # #   "todo_items": todo_items
#     # # })
#     register(request)


def add_item(request):
    date = timezone.now()
    content = request.POST["content"]
    models.Todo.objects.create(added_date=date, text=content)
    return HttpResponseRedirect("/")


def delete_item(request, id_to_delete):
    models.Todo.objects.get(id=id_to_delete).delete()
    return HttpResponseRedirect("/")


def register(request):
    if request.method == "POST":
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect("")

    else:
        form = RegisterForms()
        return render(request, "main/../register/templates/register.html", {"form": form})


def login(request):
    return render(request, 'main/../register/templates/registration/login.html')
