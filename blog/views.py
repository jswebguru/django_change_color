from .models import Index
from django.shortcuts import render


def index(request):

    image = Index.objects.get().image
    color = Index.objects.get().color

    context = {
        'image': image,
        'color': color
    }

    return render(request, 'base/home.html', context)
