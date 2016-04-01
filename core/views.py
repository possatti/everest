from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render


def index(request):
    return render(request, 'index.html')

def skills(request):
    return render(request, 'skills.html')

def coding(request):
    return render(request, 'coding.html')
