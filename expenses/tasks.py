from celery.task.schedules import crontab
from celery.decorators import periodic_task
from expenses.models import Category, Income

@periodic_task(run_every=(crontab(minute='*/1')), name='pass_day', ignore_result=True)
def pass_day():
    all_categories = Category.objects.all()
    for categori in all_categories:
        categori.next_cycle()
    all_income = Income.objects.filter(repition=True)
    for income in all_income:
        income.next_cycle()
