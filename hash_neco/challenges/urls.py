from django.urls import path
from . import views

urlpatterns = [
    path("january", views.index, name="january"),
    path("february", views.index_feb, name="february"),  # 005
]
