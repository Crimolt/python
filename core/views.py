# coding: utf-8
from django.shortcuts import render

# Create your views here.
def home(request):
        context = {'title': 'GPLAN'}
        return render(request, 'core/novo.html', context)