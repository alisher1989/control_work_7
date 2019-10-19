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




class TaskView(DetailView):
    template_name = 'poll/poll.html'
    context_object_name = 'poll'
    model = Poll
