from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),

    path('contact/', views.contact, name='contact'),#不能是path('/contact/', views.contact, name='contact'),
]

# if settings.DEBUG:#生产环境下必须移除
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)