from expenses.models import Category

def pass_day():
    all_categories = Category.objects.all()
    for categori in all_categories:
        categori.next_cycle()
