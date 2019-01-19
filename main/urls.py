from django.urls import path
from main.views import *

urlpatterns = [
    path('', EventTemplateView.as_view()),
    path('events/', EventListView.as_view()),
    path('events/week/', EventListViewWeek.as_view()),
    path('add/', EventCreateView.as_view()),
    path('update/<int:pk>', EventUpdateView.as_view()),
    path('delete/<int:pk>', EventDeleteView.as_view()),
]
