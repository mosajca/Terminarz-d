from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from main.models import Event


class EventListView(ListView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'description', 'start_date_time', 'end_date_time']
    login_url = '/login'
    success_url = '/events'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
