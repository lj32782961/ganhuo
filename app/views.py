from django.shortcuts import render, redirect,get_object_or_404
from .models import Article, Tag
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.db.models import Q

def article_list(request):
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


    #标签云
    all_tags = Tag.objects.all()

    # 检查搜索结果是否为空
    no_results = False
    if not page_obj.object_list:
        no_results = True

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'tag_filter': tag_filter,
        'all_tags': all_tags,
        'no_results': no_results,
    }
    return render(request, 'app/article_list.html', context)
    #return render(request, 'app/article_list.html', {'articles': articles})


# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'app/article_detail.html', {'article': article})

def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk) # 使用get()方法，如果不存在会抛出DoesNotExist异常
        return render(request, 'app/article_detail.html', {'article': article})
    except Article.DoesNotExist:
        return render(request, 'app/error.html')
    except Exception as e:  # 捕获其他异常
        return HttpResponse(f"发生了一个未知的错误: {e}") # 返回一个更通用的错误信息，避免泄露详细信息

def contact(request):
    return render(request, 'app/contact.html')