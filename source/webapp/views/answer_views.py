# from django.db.models import Q
# from django.shortcuts import redirect
#
# from django.urls import reverse, reverse_lazy
# from django.utils.http import urlencode
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView, FormView
#
# from webapp.forms import ArticleForm, ArticleCommentForm, SimpleSearchForm, FullSearchForm
from webapp.models import Answer
# from django.core.paginator import Paginator



class AnswerView(ListView):
    template_name = 'answer/list.html'
    context_object_name = 'answers'
    model = Answer

    #
    # def post(self, request, *args, **kwargs):
    #




