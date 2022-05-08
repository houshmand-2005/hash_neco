from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.


month_challenge = {
    "january": "this is january challenge:)",
    "february": "this is february challenge:)",
    "march": "this is march challenge:)",
}


def month_index(request, month):
    try:
        challenge_text = month_challenge[month]
        return render(request, "challenges/challenge.html", {
            "challenge_text": challenge_text,
            "nameofmonth": month,
        })
    except:
        return HttpResponseNotFound("<h1>404</h1>")


def month_index_bynumber(request, month):
    months = list(month_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>404</h1>")
    forward_month = months[month - 1]
    redirect_path = reverse("month_index", args=[
                            forward_month])  # /challenges/january
    return HttpResponseRedirect(redirect_path)


def chall_index(request):
    months = list(month_challenge.keys())
    listofmonth = ""
    for month in months:
        capitalized_month = month.capitalize()
        listofmonth += f"<li><a href='{reverse('month_index', args=[month])}'>{capitalized_month}</a></li>"
    return HttpResponse(f"<ul>{listofmonth}</ul>")
