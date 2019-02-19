from django.shortcuts import render


def index(request):
    context = {
        "username": "Lu.Biq Pan"
    }
    return render(request, 'index.html', context)
