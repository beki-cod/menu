from django.shortcuts import render
from .models import Food

# Create your views here.
def index(request):
    context = {
        'foods': Food.objects.all()
        }
    return render(request, "menu/index.html", context)

def breakfast(request):
    all_breakfast = Food.objects.filter(category="Breakfast")
    breakfast_search = request.POST.get('search')

    if breakfast_search != '' and breakfast_search is not None:
        all_breakfast = all_breakfast.filter(name_icontains=breakfast_search)

    context = {
        "breakfasts": all_breakfast
    }
    return render(request, 'menu/breakfast.html', context)


def lunch(request):
    all_lunch = Food.objects.filter(category="Lunch")
    lunch_search = request.POST.get('search')

    if lunch_search != '' and lunch_search is not None:
        all_lunch = all_lunch.filter(name_icontains=lunch_search)

    context = {
        "lunchs": all_lunch
    }
    return render(request, 'menu/lunch.html', context)


def dinner(request):
    all_dinner = Food.objects.filter(category="Dinner")
    dinner_search = request.POST.get('search')

    if dinner_search != '' and dinner_search is not None:
        all_dinner = all_dinner.filter(name_icontains=dinner_search)

    context = {
        "dinners": all_dinner
    }
    return render(request, 'menu/dinner.html', context)    