from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import HttpResponse

def article_list(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'app/article_list.html', {'articles': articles})

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