"""
ASGI config for webapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')

application = get_asgi_application()

from app.tasks import start
if os.environ.get('RUN_MAIN') != 'true':#这行代码是为了防止在测试环境中重复启动定时任务，只在实际运行环境中启动。
    start() #启动任务调度器
