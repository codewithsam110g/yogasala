from django.urls import path

from . import views
urlpatterns = [
    path("importance",views.importance,name="importance")
]