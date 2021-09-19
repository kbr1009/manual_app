from django.shortcuts import render,resolve_url, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.views.generic import DetailView, DeleteView, UpdateView
from .models import Section, Job, Item, Method, Procedure
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import UserAddForm, CreateSectionForm, CreateJobForm
from .forms import CreateJobForm, CreateItemForm
from django.urls import reverse

class SectionListView(LoginRequiredMixin, ListView):
    model = Section 
    template_name = 'manual/top.html'


class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'manual/job/job_list.html'

    def get_queryset(self):
        section = self.section = get_object_or_404(Section, pk=self.kwargs['section_id'])
        queryset = super().get_queryset().filter(section=section)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_id'] = self.section
        return context


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'manual/item/item_list.html'

    def get_queryset(self):
        job = self.job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        queryset = super().get_queryset().filter(job=job)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_id'] = self.job
        return context


class MethodListView(LoginRequiredMixin, ListView):
    model = Method
    template_name = 'manual/method/method_list.html'

    def get_queryset(self):
        item = self.item = get_object_or_404(Item, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(item=item)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = self.item
        return context



#Auth
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



#EDIT
class EditSectionListView(LoginRequiredMixin, ListView):
    model = Section 
    template_name = 'manual/edit/list.html'

    def post(self, request):
        post_pks = request.POST.getlist('delete')
        Section.objects.filter(pk__in=post_pks).delete()
        return redirect("manual:edit_section_list") 

class CreateSectionView(LoginRequiredMixin, CreateView):
    model = Section
    template_name = "manual/edit/create.html"
    form_class = CreateSectionForm

    def get_success_url(self):
        return reverse_lazy("manual:edit_section_list") 


class UpdateSectionView(LoginRequiredMixin, UpdateView):
    template_name = 'manual/edit/update.html'
    model = Section
    fields = ['section_name',]
 
    def get_form(self):
        form = super(UpdateSectionView, self).get_form()
        form.fields['section_name'].label = '編集するセクション名'
        return form

    def get_success_url(self):
        return reverse_lazy("manual:edit_section_list") 


class EditJobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'manual/edit/job/list.html'

    def get_queryset(self):
        section = self.section = get_object_or_404(Section, pk=self.kwargs['section_id'])
        queryset = super().get_queryset().filter(section=section)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_pk'] = self.section
        return context

    def post(self, request, section_id):
        post_pks = request.POST.getlist('delete')
        Job.objects.filter(pk__in=post_pks).delete()
        return redirect('manual:edit_job_list', section_id)


class CreateJobView(LoginRequiredMixin, CreateView):
    template_name = "manual/edit/job/create.html"
    form_class = CreateJobForm 

    def get_context_data(self, **kwargs):
        section = self.section = get_object_or_404(Section, pk=self.kwargs['section_id'])
        context = super(CreateJobView, self).get_context_data(**kwargs)
        context['section_pk'] = self.section
        return context

    def form_valid(self, form):
        section_instance = get_object_or_404(Section, pk=self.kwargs['section_id'])
        form.instance.section = section_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('manual:edit_job_list', kwargs={
            'section_id': self.kwargs.get('section_id')
            }
        )


class UpdateJobView(LoginRequiredMixin, UpdateView):
    template_name = 'manual/edit/job/update.html'
    model = Job
    fields = ['job_name',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_pk'] = self.object.section_id 
        return context

    def get_form(self):
        form = super(UpdateJobView, self).get_form()
        form.fields['job_name'].label = '編集する作業名'
        return form

    def get_success_url(self):
        return reverse('manual:edit_job_list', kwargs={
            'section_id': self.object.section_id
            }
        )


class EditItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'manual/edit/item/list.html'

    def get_queryset(self):
        job = self.job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        queryset = super().get_queryset().filter(job=job)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_pk'] = self.job
        return context

    def post(self, request, section_id, job_id):
        post_pks = request.POST.getlist('delete')
        Item.objects.filter(pk__in=post_pks).delete()
        return redirect('manual:edit_item_list', section_id, job_id)


class CreateItemView(LoginRequiredMixin, CreateView):
    template_name = "manual/edit/item/create.html"
    form_class = CreateItemForm

    def get_context_data(self, **kwargs):
        job = self.job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        context = super(CreateItemView, self).get_context_data(**kwargs)
        context['job_pk'] = self.job
        return context

    def form_valid(self, form):
        job_instance = get_object_or_404(Job, pk=self.kwargs['job_id'])
        form.instance.job = job_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('manual:edit_item_list', kwargs={
            'section_id': self.kwargs.get('section_id'),
            'job_id': self.kwargs.get('job_id')
            }
        )


class UpdateItemView(LoginRequiredMixin, UpdateView):
    template_name = 'manual/edit/item/update.html'
    model = Item
    fields = ['item_name', 'purpose', 'success',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_pk'] = self.object.job
        return context

    def get_form(self):
        form = super(UpdateItemView, self).get_form()
        form.fields['item_name'].label = '編集する項目名'
        return form

    def get_success_url(self):
        return reverse('manual:edit_item_list', kwargs={
            'job_id': self.object.job.id,
            'section_id': self.object.job.section.id
            }
        )


"""methodlist"""

class EditMethodListView(LoginRequiredMixin, ListView):
    model = Method
    template_name = 'manual/edit/method/list.html'

    def get_queryset(self):
        item = self.item = get_object_or_404(Item, pk=self.kwargs['item_id'])
        queryset = super().get_queryset().filter(item=item)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_pk'] = self.item
        return context

"""
///delete
    def post(self, request, section_id, job_id):
        post_pks = request.POST.getlist('delete')
        Item.objects.filter(pk__in=post_pks).delete()
        return redirect('manual:edit_item_list', section_id, job_id)
"""

"""
class CreateItemView(LoginRequiredMixin, CreateView):
    template_name = "manual/edit/item/create.html"
    form_class = CreateItemForm

    def get_context_data(self, **kwargs):
        job = self.job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        context = super(CreateItemView, self).get_context_data(**kwargs)
        context['job_pk'] = self.job
        return context

    def form_valid(self, form):
        job_instance = get_object_or_404(Job, pk=self.kwargs['job_id'])
        form.instance.job = job_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('manual:edit_item_list', kwargs={
            'section_id': self.kwargs.get('section_id'),
            'job_id': self.kwargs.get('job_id')
            }
        )

class UpdateItemView(LoginRequiredMixin, UpdateView):
    template_name = 'manual/edit/item/update.html'
    model = Item
    fields = ['item_name', 'purpose', 'success',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_pk'] = self.object.job
        return context

    def get_form(self):
        form = super(UpdateItemView, self).get_form()
        form.fields['item_name'].label = '編集する項目名'
        return form

    def get_success_url(self):
        return reverse('manual:edit_item_list', kwargs={
            'job_id': self.object.job.id,
            'section_id': self.object.job.section.id
            }
        )
"""
