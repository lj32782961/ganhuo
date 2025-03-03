from django.conf import settings

def current_language_name(request):
    # 从 LANGUAGES 中获取当前语言的名称
    current_language_name = dict(settings.LANGUAGES).get(request.LANGUAGE_CODE, '')
    return {
        'current_language_name': current_language_name,
    }