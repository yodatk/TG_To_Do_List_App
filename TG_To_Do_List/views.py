from django.shortcuts import render
from django.utils import timezone
from TG_To_Do_List import models
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    """
    rendering the home page
    :param request: Request param
    :return: rendered page of the home page
    """
    todo_items = models.Todo.objects.all().order_by("-added_date")
    return render(request, 'main/list_editing_page.html', {
        "todo_items": todo_items
    })


def add_item(request):
    date = timezone.now()
    content = request.POST["content"]
    models.Todo.objects.create(added_date=date, text=content)
    return HttpResponseRedirect("/")


def delete_item(request, id_to_delete):
    models.Todo.objects.get(id=id_to_delete).delete()
    return HttpResponseRedirect("/")
