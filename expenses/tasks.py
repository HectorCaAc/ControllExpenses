from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

from expenses.models import Category, Income

@sched.scheduled_job('interval', minutes=2)
def pass_day():
    all_categories = Category.objects.all()
    for categori in all_categories:
        categori.next_cycle()
    all_income = Income.objects.filter(repition=True)
    for income in all_income:
        income.next_cycle()
