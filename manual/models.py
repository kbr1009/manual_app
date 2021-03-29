from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey


class Section(SortableMixin):
    section_name = models.CharField(
            verbose_name='1.セクション', 
            max_length=50, 
            blank=False, 
            null=True
            )
    the_order = models.PositiveIntegerField(
            default=0, 
            editable=False, 
            db_index=True
            )

    class Meta:
        verbose_name = '1.セクション'
        verbose_name_plural = '1.セクション'
        ordering = ["the_order"]

    def __str__(self):
        return self.section_name


class Job(SortableMixin):
    job_name = models.CharField(
            verbose_name='2.作業名', 
            max_length=50, 
            blank=False, 
            null=True
            )
    section = models.ForeignKey(
            Section, 
            verbose_name='属する項目', 
            on_delete=models.CASCADE, 
            blank=False, 
            null=True
            )
    the_order = models.PositiveIntegerField(
            default=0, 
            editable=False, 
            db_index=True
            )

    class Meta:
        verbose_name = '2.作業名'
        verbose_name_plural = '2.作業名' 
        ordering = ["the_order"]

    def __str__(self):
        return f"{self.section} >> {self.job_name}"


#作業項目
class Item(SortableMixin):
    item_name = models.CharField(
            verbose_name='3.作業項目', 
            max_length=50, 
            blank=False, 
            null=True
            )
    purpose = models.CharField(
            verbose_name='目的', 
            max_length=100, 
            blank=True, 
            null=True
            )
    success = models.CharField(
            verbose_name='達成基準', 
            max_length=100, 
            blank=True, 
            null=True
            )
    job = models.ForeignKey(
            Job, 
            verbose_name='属する項目', 
            on_delete=models.CASCADE, 
            blank=False, 
            null=True
            )
    the_order = models.PositiveIntegerField(
            default=0, 
            editable=False, 
            db_index=True
            )

    class Meta:
        verbose_name = '3.作業項目'
        verbose_name_plural = '3.作業項目' 
        ordering = ["the_order"]


    def __str__(self):
        return f"{self.job} >> {self.item_name}"


#作業方法
class Method(SortableMixin):
    method_name = models.CharField(
            verbose_name='4.作業方法',
            max_length=50, blank=False, 
            null=True
            )
    item = models.ForeignKey(
            Item, 
            verbose_name='属する項目',
            on_delete=models.CASCADE, 
            blank=False, 
            null=True,
            related_name='method'
            )
    the_order = models.PositiveIntegerField(
            default=0, 
            editable=False, 
            db_index=True
            )

    class Meta:
        verbose_name = '4.作業方法'
        verbose_name_plural = '4.作業方法'
        ordering = ["the_order"]

    def __str__(self):
        return f"{self.item} >> {self.method_name}"


#作業手順
class Procedure(SortableMixin):
    procedure_name = models.TextField(
            verbose_name='5.作業手順', 
            max_length=200, 
            blank=False, 
            null=True
            )
    point = models.TextField(
            verbose_name='ポイント', 
            max_length=200, 
            blank=True, 
            null=True
            )
    caution = models.TextField(
            verbose_name='注意点', 
            max_length=200, 
            blank=True, 
            null=True
            )
    tips = models.TextField(
            verbose_name='コツ', 
            max_length=200, 
            blank=True, 
            null=True
            ) 
    img = models.ImageField(
            verbose_name='画像', 
            upload_to='img/', 
            blank=True, 
            null=True
            )
    video = models.FileField(
            verbose_name='動画', 
            upload_to='video/', 
            blank=True, 
            null=True
            )
    method = models.ForeignKey(
            Method, 
            verbose_name='属する項目',
            on_delete=models.CASCADE, 
            blank=False, 
            null=True,
            related_name='procedure'
            )
    the_order = models.PositiveIntegerField(
            default=0, 
            editable=False, 
            db_index=True
            )

    class Meta:
        verbose_name = '5.作業手順'
        verbose_name_plural = '5.作業手順'
        ordering = ["the_order"]

    def __str__(self):
        return self.procedure_name
