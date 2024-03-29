from django.shortcuts import render, reverse

DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, г": 0.3,
        "сыр, г": 0.05,
    },
    "buter": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
    "sweet_bread": {
        "братишка, шт.": 1,
        "покушать, шт.": 2,
        "принес, шт.": 3,
    },
}


def home_view(request):
    pages = {
        "Омлет": reverse("cook_dish", kwargs={"dish": "omlet"}),
        "Паста": reverse("cook_dish", kwargs={"dish": "pasta"}),
        "Бутерброд": reverse("cook_dish", kwargs={"dish": "buter"}),
        "Сладкий хлеб": reverse("cook_dish", kwargs={"dish": "sweet_bread"}),
    }
    context = {"pages": pages}

    return render(request, "calculator/home.html", context)


def cook_dish(request, dish):
    servings = int(request.GET.get("servings", 1))
    recipe = DATA.get(dish)

    for ingr_name, ingr_amnt in recipe.items():
        recipe[ingr_name] = ingr_amnt * servings

    context = {"recipe": recipe, "pers": servings}
    return render(request, "calculator/index.html", context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
