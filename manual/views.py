from django.shortcuts import render,resolve_url, get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic import DetailView, DeleteView
from .models import Section, Job, Item, Method, Procedure
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import UserAddForm, CreateSectionForm
from .forms import CreateJobForm

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


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'manual/users/user_detail.html'


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'manual/users/user_delete.html'
    success_url = reverse_lazy('manual:user_list')


class UserCreateView(CreateView):
    model = User
    template_name = "manual/users/user_add.html"
    form_class = UserAddForm
    success_url = reverse_lazy("manual:user_list")

    def get_success_url(self):
        return reverse_lazy("manual:user_list") 


class CreateSectionListView(LoginRequiredMixin, ListView):
    model = Section 
    template_name = 'manual/create/list.html'


class CreateSectionView(CreateView):
    model = Section
    template_name = "manual/create/create.html"
    form_class = CreateSectionForm
    success_url = reverse_lazy("manual:create_section_list")
    
    def get_success_url(self):
        return reverse_lazy("manual:create_section_list") 


class CreateJobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'manual/create/job/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = self.section
        return context

    def get_queryset(self):
        section = self.section = get_object_or_404(Section, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(section=section)
        return queryset


class CreateJobView(CreateView):
    model = Job
    template_name = "manual/create/job/create.html"
    form_class = CreateJobForm

    def get_context_data(self, **kwargs):
        return CreateView.get_context_data(self, **kwargs)
    
    def form_valid(self, form):
        return CreateView.form_valid(self, form);
    
    def get_success_url(self):
        return reverse_lazy('manual:top')

"""
#https://teratail.com/questions/293693　を参照
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        section = Section.objects.get(id = self.kwargs['section_name'])
        form.instance.section_id= section.id
        form.save()


    def get_success_url(self):
        return reverse_lazy("manual:top") 
"""
"""
    def form_valid(self, form):
        form.instance.section_id = self.request.user.id
        return super(CreateJobView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("manual:top") 
"""
