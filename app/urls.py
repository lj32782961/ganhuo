from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('switch_language/<str:lang_code>/', views.switch_language, name='switch_language'),

    path('contact/', views.contact, name='contact'),#不能是path('/contact/', views.contact, name='contact'),
]


# if settings.DEBUG:#生产环境下必须移除
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

