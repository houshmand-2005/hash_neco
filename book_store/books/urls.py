from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("<int:id>", views.book_page, name="book_page")
]