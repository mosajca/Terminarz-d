from django.urls import path
from main.views import EventListView, EventCreateView

urlpatterns = [
    path('events/', EventListView.as_view()),
    path('add/', EventCreateView.as_view()),
]
