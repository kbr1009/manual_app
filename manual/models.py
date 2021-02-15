from django.db import models
from adminsortable.models import SortableMixin

class Section(models.Model):
    section_name = models.CharField(verbose_name='セクション', max_length=50, blank=False, null=True)

    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name = 'セクション'
        verbose_name_plural = 'セクション'


class Job(models.Model):
    job_name = models.CharField(verbose_name='作業名', max_length=50, blank=False, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.job_name

    class Meta:
        verbose_name = '作業名'
        verbose_name_plural = '作業名'


#作業項目
class Item(models.Model):
    item_name = models.CharField(verbose_name='作業項目', max_length=50, blank=False, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = '作業項目'
        verbose_name_plural = '作業項目' 


#作業方法
class Method(models.Model):
    method_name = models.CharField(verbose_name='作業方法', max_length=50, blank=False, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.method_name

    class Meta:
        verbose_name = '作業方法'
        verbose_name_plural = '作業方法'


#作業手順
class Procedure(models.Model):
    procedure_name = models.TextField(verbose_name='作業手順', max_length=50, blank=False, null=True)
    img = models.ImageField(verbose_name='作業映像', upload_to='img/', blank=True, null=True)
    video = models.FileField(verbose_name='作業動画', upload_to='video/', blank=True, null=True)
    point = models.TextField(verbose_name='ポイント', max_length=50, blank=True, null=True)
    caution = models.TextField(verbose_name='注意点', max_length=50, blank=True, null=True)
    tips = models.TextField(verbose_name='コツ', max_length=50, blank=True, null=True) 
    method = models.ForeignKey(Method, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.procedure_name

    class Meta:
        verbose_name = '作業手順'
        verbose_name_plural = '作業手順'

"""
class Annotation(models.Model):
    point = models.TextField(verbose_name='ポイント', max_length=50, blank=True, null=True)
    caution = models.TextField(verbose_name='注意点', max_length=50, blank=True, null=True)
    tips = models.TextField(verbose_name='コツ', max_length=50, blank=True, null=True) 
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.point_name

    class Meta:
        verbose_name = 'ポイント'
        verbose_name_plural = 'ポイント'
"""
