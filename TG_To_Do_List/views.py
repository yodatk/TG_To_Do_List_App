from django.shortcuts import render
from django.utils import timezone
from TG_To_Do_List import models


# Create your views here.
def home(request):
    """
    rendering the home page
    :param request: Request param
    :return: rendered page of the home page
    """
    return render(request, template_name='base.html')


def add_item(request):
    date = timezone.now()
    content = request.POST["content"]
    models.Todo.objects.create(added_date=date, text=content)
    return render(request, template_name='base.html')
