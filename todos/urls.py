from django.urls import path

from . import views

app_name = "todos"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cerate", views.create, name="create"),
    path("update", views.update, name="update"),
]
