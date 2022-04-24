import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world. You're at the hash_neco index.")


# def index_feb(request):
#     return HttpResponse("this is february challenge:)")  # 005

# 006
def month_index(request, month):
    if month == "january":
        challenge_text = ("this is january challenge:)")
    elif month == "february":
        challenge_text = ("this is february challenge:)")
    elif month == "march":
        challenge_text = ("this is march challenge:)")
    else:
        return HttpResponseNotFound("<h1>404</h1>")
    return HttpResponse(challenge_text)
