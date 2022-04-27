from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world. You're at the hash_neco index.")


# def index_feb(request):
#     return HttpResponse("this is february challenge:)")  # 005

# 006

month_challenge = {
    "january": "this is january challenge:)",
    "february": "this is february challenge:)",
    "march": "this is march challenge:)",
}


def month_index(request, month):
    # if month == "january":
    #     challenge_text = "this is january challenge:)"
    # elif month == "february":
    #     challenge_text = "this is february challenge:)"
    # elif month == "march":
    #     challenge_text = "this is march challenge:)"
    # else:
    #     return HttpResponseNotFound("<h1>404</h1>")
    # return HttpResponse(challenge_text)
    #  008
    try:
        challenge_text = month_challenge[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>404</h1>")
# 007 and 008


def month_index_bynumber(request, month):
    months = list(month_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>404</h1>")
    forward_month = months[month - 1]
    redirect_path = reverse("month_index", args=[forward_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)
