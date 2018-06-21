from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from sgce.core.forms import EventForm
from sgce.core.models import Event


@login_required
def index(request):
    return render(request, 'core/index.html')


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'core/event/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = super(EventListView, self).get_queryset()
        user = self.request.user
        return queryset if user.is_superuser else queryset.filter(created_by=self.request.user)


class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    raise_exception = True
    template_name = 'core/event/event_form.html'
    success_url = reverse_lazy('core:event-list')
    success_message = "O evento %(name)s foi criado com sucesso."

    # user_passes_test
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.profile.is_manager()

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventForm
    raise_exception = True
    template_name = 'core/event/event_form.html'
    success_url = reverse_lazy('core:event-list')
    success_message = "O evento %(name)s foi atualizado com sucesso."

    # user_passes_test
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.profile.is_manager()


def event_detail(request, slug): pass