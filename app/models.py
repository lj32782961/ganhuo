from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    abstract = models.TextField(max_length=200, verbose_name='摘要',default=' ')
    content = RichTextUploadingField(verbose_name='内容')
    image = models.ImageField(upload_to='img/', blank=True, null=True,verbose_name='图片')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    views = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    tag = models.ManyToManyField(Tag, blank=True)
    source = models.CharField(max_length=200, verbose_name="来源")

    class Meta:
        verbose_name = '文章列表'
        verbose_name_plural = '文章列表'

    def __str__(self):
        #return f"标题{self.title}，摘要：{self.content[:10]}，来源：{self.source}，创建时间：{self.pub_date} "
        return f"{self.title}, 创建时间：{self.pub_date} "
    

