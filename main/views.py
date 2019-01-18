from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from main.models import Event


class EventTemplateView(TemplateView):
    template_name = 'main/index.html'


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    login_url = '/login'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'description', 'start_date_time', 'end_date_time']
    login_url = '/login'
    success_url = '/events'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name', 'description', 'start_date_time', 'end_date_time']
    login_url = '/login'
    success_url = '/events'
    template_name_suffix = '_update_form'


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events'
