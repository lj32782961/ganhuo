from django.shortcuts import render, redirect,get_object_or_404
from .models import Article, Tag
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.db.models import Q
import datetime
from django.utils import timezone
from django.conf import settings
from django.utils.translation import activate

def article_list(request):
    # 获取热门文章（可根据阅读量排序）
    hot_articles = Article.objects.all().order_by('-views')[:5]

    search_query = request.GET.get('q', '')
    tag_filter = request.GET.get('tag', '')

    articles = Article.objects.all().order_by('-pub_date')

    # 搜索过滤
    if search_query:
        query_obj = Q()
        query_obj |=Q(title__icontains=search_query)|Q(content__icontains=search_query)

        articles = articles.filter(query_obj).order_by('-pub_date')


    # 标签过滤
    if tag_filter:
        articles = articles.filter(tag__name=tag_filter).order_by('-pub_date')

    # 分页
    paginator = Paginator(articles, 10)  # 每页10条
    page_number = request.GET.get('page')
    # 防止在输入无效页码时程序崩溃。 现在如果输入的页码无效，则会显示第一页或最后一页的内容。
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)


    # 检查搜索结果是否为空
    no_results = False
    if not page_obj.object_list:
        no_results = True

    #标签云
    all_tags = Tag.objects.all()


    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'tag_filter': tag_filter,
        'all_tags': all_tags,
        'no_results': no_results,
        'hot_articles':hot_articles,
    }
    return render(request, 'app/article_list.html', context)
    #return render(request, 'app/article_list.html', {'articles': articles})


# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'app/article_detail.html', {'article': article})

def article_detail(request, pk):
    # 获取热门文章（可根据阅读量排序）
    hot_articles = Article.objects.all().order_by('-views')[:5]
    #标签云
    all_tags = Tag.objects.all()
    try:
        article = Article.objects.get(pk=pk) # 使用get()方法，如果不存在会抛出DoesNotExist异常
        article.views = article.views+1
        article.save(update_fields=['views'])  # 只更新views字段，提高效率

        context = {
        'article': article,
        'all_tags': all_tags,
        'hot_articles':hot_articles,
    }
        return render(request, 'app/article_detail.html', context)
    except Article.DoesNotExist:
        return render(request, 'app/error.html')
    except Exception as e:  # 捕获其他异常
        return HttpResponse(f"发生了一个未知的错误: {e}") # 返回一个更通用的错误信息，避免泄露详细信息

def contact(request):
    return render(request, 'app/contact.html')

from django.utils import translation
from django.http import HttpResponseRedirect
def switch_language(request, lang_code):
    """
    切换语言并存入 session
    """
    if lang_code in dict(settings.LANGUAGES).keys():  # 确保 lang_code 是支持的语言
        # activate(lang_code)
        # request.session['django_language'] = lang_code
        # 激活当前请求的语言
        translation.activate(lang_code)
        # 存入Session，供后续请求使用
        request.session['django_language'] = lang_code
        # 创建重定向响应
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        # 将语言代码存入Cookie
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def create_german_article():
    title = f"自动生成的标题 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    abstract = "这是一篇自动生成的摘要。"
    content = "<p>这是一篇自动生成的RichText内容。</p>"  # RichTextUploadingField 需要 HTML
    source = "本站"

    # 查找或创建标签 (例如，创建一个名为'自动生成'的标签)
    tag, created = Tag.objects.get_or_create(name='自动生成', slug='auto-generated')

    article = Article(
        title=title,
        abstract=abstract,
        content=content,
        source=source,
    )
    article.save()
    article.tag.add(tag) # 使用 add() 方法添加标签

from django.utils.translation import gettext as _
