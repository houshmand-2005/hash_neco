from django.urls import path
from . import views
urlpatterns = [
    path("", views.review),
    path("thank_you", views.thank_you)
]