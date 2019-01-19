from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from main.models import Event
import datetime


class EventTemplateView(TemplateView):
    template_name = 'main/index.html'


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    login_url = '/login'
    current = 0
    day = None

    def get_queryset(self):
        try:
            self.current = int(self.request.GET.get('n', 0))
        except:
            self.current = 0
        self.day = timezone.make_aware(datetime.datetime.today() + datetime.timedelta(days=self.current))
        return super().get_queryset().filter(user=self.request.user).filter(start_date_time__date=self.day)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['day'] = self.day.date()
        context['prev'] = self.current - 1
        context['next'] = self.current + 1
        return context


class EventListViewWeek(LoginRequiredMixin, ListView):
    model = Event
    login_url = '/login'
    current = 0
    start_week = None
    end_week = None

    def get_queryset(self):
        try:
            self.current = int(self.request.GET.get('n', 0))
        except:
            self.current = 0
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday() - self.current * 7)
        sunday = monday + datetime.timedelta(days=6)
        self.start_week = timezone.make_aware(datetime.datetime.combine(monday, datetime.time.min))
        self.end_week = timezone.make_aware(datetime.datetime.combine(sunday, datetime.time.max))
        return super().get_queryset().filter(user=self.request.user).filter(
            start_date_time__range=(self.start_week, self.end_week))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['start_week'] = self.start_week.date()
        context['end_week'] = self.end_week.date()
        context['prev'] = self.current - 1
        context['next'] = self.current + 1
        return context


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
