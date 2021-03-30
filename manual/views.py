from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import ListView
=======
from django.views.generic import TemplateView, ListView
>>>>>>> de25bed57219ea1c03c93357c020314a79647dd0
from .models import Section, Job, Item, Method, Procedure
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import get_object_or_404


<<<<<<< HEAD
class SectionListView(LoginRequiredMixin, ListView):
    model = Section 
    template_name = 'manual/top.html'
=======
class TopView(LoginRequiredMixin, TemplateView):
    template_name = 'manual/top.html'


class SectionListView(LoginRequiredMixin, ListView):
    model = Section 
    template_name = 'manual/section/section_list.html'
>>>>>>> de25bed57219ea1c03c93357c020314a79647dd0


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
