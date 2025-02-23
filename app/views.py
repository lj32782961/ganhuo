from django.shortcuts import render, get_object_or_404
from .models import Article, Tag
from django.http import HttpResponse
from django.core.paginator import Paginator
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
        articles = articles.filter(tag__name=tag_filter)

    # 分页
    paginator = Paginator(articles, 10)  # 每页10条
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #标签云
    all_tags = Tag.objects.all()

    #return render(request, 'app/article_list.html', {'articles': articles})
    return render(request, 'app/article_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'tag_filter': tag_filter,
        'all_tags': all_tags
    })



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