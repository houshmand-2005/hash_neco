from django.urls import path
from . import views
urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank_you", views.ThankYou.as_view()),
    path("reviews", views.ReviewList.as_view()),
    path("reviews/<int:pk>", views.DetailReview.as_view(), name="reviews_page")
]