from django.shortcuts import render
from .models import ContatoModel

def index(request):
    context = {'contato': ContatoModel.objects.all()}
    return render(request, 'index.html', context)