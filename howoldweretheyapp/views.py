
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddCelebrity
from .models import Celebrity
from .forms import AddCelebrity

def index(request):
    return HttpResponse("<h1>Hello, world !</h1>")


def howoldwerethey(request):
    form = AddCelebrity()
    celebrity_list = Celebrity.objects.order_by('id')
    context = {'celebrity_list': celebrity_list, 'form': form}
    #context = {}
    return render(request, 'index.html', context)

