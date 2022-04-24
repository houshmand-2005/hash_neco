import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the hash_neco index.")


def index_feb(request):
    return HttpResponse("this is february challenge:)") # 005
