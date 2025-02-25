from django.contrib import admin
from .models import Article, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from django.utils.text import slugify

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('title', 'abstract', 'views', 'pub_date', 'source', 'get_tags')
    search_fields = ('pub_date', 'source', 'get_tags')
    filter_horizontal = ('tag',)  # 添加多选标签界面

    def get_tags(self, obj):
        return ", ".join([str(tag) for tag in obj.tag.all()])
    get_tags.short_description = '标签'


# class MyAdminSite(AdminSite):
#     site_header = _("管理后台")  # 替换成自定义的标题
#     site_title = _("管理系统")  # 替换成自定义的标题
#     index_title = _("欢迎使用管理系统")  # 替换成自定义的标题

# # 使用自定义的 AdminSite
# admin_site = MyAdminSite(name='myadmin')

# # 手动注册用户和组
# admin_site.register(Article)
# admin_site.register(User)
# admin_site.register(Group)

# # 让默认的 admin.site 使用这个 MyAdminSite
# admin.site = admin_site
# admin.autodiscover()