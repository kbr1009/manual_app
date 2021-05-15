from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Section, Job, Item, Method, Procedure
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class SectionListView(LoginRequiredMixin, ListView):
    model = Section 
    template_name = 'manual/top.html'


class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'manual/job/job_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = self.section
        return context

    def get_queryset(self):
        section = self.section = get_object_or_404(Section, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(section=section)
        return queryset


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'manual/item/item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = self.job
        return context

    def get_queryset(self):
        job = self.job = get_object_or_404(Job, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(job=job)
        return queryset


class MethodListView(LoginRequiredMixin, ListView):
    model = Method
    template_name = 'manual/method/method_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = self.item
        return context

    def get_queryset(self):
        item = self.item = get_object_or_404(Item, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(item=item)
        return queryset

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'manual/users/user_list.html'

class UserCreateView(CreateView):
  model = User
  template_name = "manual/users/user_add.html"
  form_class = UserCreationForm
  success_url = reverse_lazy('manual:user_list') # urls.pyのnameを指定
  # template_nameのデフォルトはtemplates/auth/user_form.html
  def get_success_url(self):
      return reverse_lazy('manual:user_list') 
