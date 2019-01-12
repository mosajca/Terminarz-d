from django.urls import path
from main.views import EventListView, EventCreateView, EventUpdateView, EventDeleteView

urlpatterns = [
    path('events/', EventListView.as_view()),
    path('add/', EventCreateView.as_view()),
    path('update/<int:pk>', EventUpdateView.as_view()),
    path('delete/<int:pk>', EventDeleteView.as_view()),
]
