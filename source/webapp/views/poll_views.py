from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode

from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Poll
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 4
    paginate_orphans = 1




class PollView(DetailView):
    template_name = 'poll/poll.html'
    context_object_name = 'poll'
    model = Poll


class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('index')

