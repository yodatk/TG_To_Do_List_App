from django.shortcuts import render
from django.utils import timezone
from TG_To_Do_List import models
from django.http import HttpResponseRedirect


def main(request):
    """
     Render the current logged in user to it's list
    :param request: Http request
    :return: If the form is valid, connect the user to it's list.
            Otherwise , stays in login page and shows what is wrong
    """
    if request.user.is_authenticated:
        username = request.user.username
        todo_items = models.Todo.objects.all().filter(user__username=username).order_by("-added_date")
        return render(request, 'main/list_editing_page.html', {"todo_items": todo_items})
    else:
        form = request.POST
        render(request, "registration/login.html", {"form": form})


def add_item(request):
    """
    Adding new item to the current user's list.
    :param request: Http request
    :return: Rendering the same user's list page, with the new item
    """
    date = timezone.now()
    content = request.POST["content"]
    user = request.user
    models.Todo.objects.create(user=user, added_date=date, text=content)
    return HttpResponseRedirect('/connected/')


def delete_item(request, id_to_delete):
    """
    Deleting a given item from the current user's list.
    :param request: Https request
    :param id_to_delete: Id to delete
    :return:
    """
    models.Todo.objects.get(id=id_to_delete).delete()
    return HttpResponseRedirect('/connected/')


def login(request):
    """
    Connecting the user to the homepage
    :param request: Http request
    :return: The home page (login page)
    """
    return HttpResponseRedirect("login/")
