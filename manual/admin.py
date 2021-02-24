from django.contrib import admin
from .models import Section, Job, Item, Method, Procedure
from adminsortable.admin import SortableAdmin


class SectionAdmin(SortableAdmin):
    list_display = ('id', 'section_name')
    list_display_links = ('id', 'section_name')


class JobAdmin(SortableAdmin):
    list_display = ('id', 'job_name','section')
    list_display_links = ('id', 'job_name')


class ItemAdmin(SortableAdmin):
    list_display = ('id', 'item_name', 'item_section', 'job')
    list_display_links = ('id', 'item_name')


class MethodAdmin(SortableAdmin):
    list_display = ('id', 'method_name','method_section', 'method_job', 'item')
    list_display_links = ('id', 'method_name')


class ProcedureAdmin(SortableAdmin):
    list_display = ('id', 'procedure_name', 'procedure_section', 'procedure_job', 'procedure_item', 'method')
    list_display_links = ('id', 'procedure_name')


admin.site.register(Section, SectionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Method, MethodAdmin)
admin.site.register(Procedure, ProcedureAdmin)
