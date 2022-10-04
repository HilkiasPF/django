from django.shortcuts import render

def index(request):
    context = {'opa': 'ta'}
    return render(request, 'index.html', context)