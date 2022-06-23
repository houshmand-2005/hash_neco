from django.urls import path
from . import views
urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank_you", views.ThankYou.as_view()),
    path("reviews", views.ReviewList.as_view())
]