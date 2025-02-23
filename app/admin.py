from django.contrib import admin
from .models import Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('title', 'pub_date', 'update_date')
    search_fields = ('title', 'content')