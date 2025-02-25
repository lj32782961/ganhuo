from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.background import BackgroundScheduler
from .views import create_german_article  # 导入上面创建文章的函数

def start():
    # scheduler = BackgroundScheduler()
    scheduler = BackgroundScheduler(jobstores={'default': DjangoJobStore()})
    scheduler.add_job(create_german_article, 'interval', days=1) #每天运行一次
    scheduler.start()