# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})
