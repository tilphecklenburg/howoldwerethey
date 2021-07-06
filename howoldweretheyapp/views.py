
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddCelebrity
from .models import Celebrity

def index(request):
    return HttpResponse("<h1>Hello, world !</h1>")


def howoldwerethey(request):
    celebrity_list = Celebrity.objects.order_by('id')
    context = {'celebrity_list': celebrity_list}
    return render(request, 'index.html', context)

