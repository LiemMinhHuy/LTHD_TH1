from django.contrib import admin
from courses.models import Category, Course
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets \
    import CKEditorUploadingWidget


# Register your models here.

class CourseForm(forms.ModelForm):
    desription = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        field    = '__all__'


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    list_filter = ['id', 'created_date', 'name']
    readonly_fields = ['my_image']


    def my_image(self, instance):
        if instance:
            return mark_safe(f"<img width='120' src='/static/{instance.image.name}'/>")

    class Media:
        css = {
            'add': ('/static/css/style.css',)
        }


admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
