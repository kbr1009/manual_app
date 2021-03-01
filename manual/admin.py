from django.contrib import admin
from .models import Section, Job, Item, Method, Procedure
from adminsortable.admin import SortableAdmin


class SectionAdmin(SortableAdmin):
    list_display = ('id', 'section_name')
    list_display_links = ('id', 'section_name')


class JobAdmin(SortableAdmin):
    list_display = ('id', 'job_name', 'section')
    list_display_links = ('id', 'job_name')


class ItemAdmin(SortableAdmin):
    list_display = ('id', 'item_name', 'relate_section','job')
    list_display_links = ('id', 'item_name')

    def relate_section(self, obj):
        return obj.job.section
    relate_section.short_description = 'セクション'
    relate_section.admin_order_field = 'relate_section'


class MethodAdmin(SortableAdmin):
    list_display = ('id', 'method_name', 'relate_section', 'relate_job', 'item')
    list_display_links = ('id', 'method_name')

    def relate_section(self, obj):
        return obj.item.job.section
    relate_section.short_description = 'セクション'
    relate_section.admin_order_field = 'relate_section'

    def relate_job(self, obj):
        return obj.item.job
    relate_job.short_description = '作業名'
    relate_job.admin_order_field = 'relate_job'


class ProcedureAdmin(SortableAdmin):
    list_display = ('id', 'procedure_name', 'relate_section', 'relate_job', 'relate_item', 'method')
    list_display_links = ('id', 'procedure_name')

    def relate_section(self, obj):
        return obj.method.item.job.section
    relate_section.short_description = 'セクション'
    relate_section.admin_order_field = 'relate_section'

    def relate_job(self, obj):
        return obj.method.item.job
    relate_job.short_description = '作業名'
    relate_job.admin_order_field = 'relate_job'

    def relate_item(self, obj):
        return obj.method.item
    relate_item.short_description = '作業項目'
    relate_item.admin_order_field = 'relate_item'


admin.site.register(Section, SectionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Method, MethodAdmin)
admin.site.register(Procedure, ProcedureAdmin)
