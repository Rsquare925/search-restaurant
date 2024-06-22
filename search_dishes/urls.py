from django.urls import path
from search_dishes import views

urlpatterns = [
    path("", views.search, name="search"),
]
