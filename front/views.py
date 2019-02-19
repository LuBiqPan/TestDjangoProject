from django.shortcuts import render


def index(request):
    context = {
        "username": "Lu.Biq La"
    }
    return render(request, 'index.html', context)
