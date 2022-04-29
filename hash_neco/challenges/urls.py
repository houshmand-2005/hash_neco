from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index, name="january"),
    # path("february", views.index_feb, name="february"),  # 005
    path("<int:month>", views.month_index_bynumber, name="month_index"),  # 007
    path("<str:month>", views.month_index, name="month_index"),  # 006
    path("", views.chall_index, name="index"),
]
