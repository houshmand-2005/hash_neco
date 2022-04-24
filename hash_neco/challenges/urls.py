from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index, name="january"),
    # path("february", views.index_feb, name="february"),  # 005
    path("<month>", views.month_index, name="month_index"),  # 006
]
