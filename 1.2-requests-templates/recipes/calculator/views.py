from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def dish_view(request, dish):
    context = {'recipe':{}}
    ingredients = DATA.get(dish)
    if not ingredients:
        return render(request, 'calculator/index.html', context)
    servings = int(request.GET.get('servings', 1))
    if servings < 1:
        servings = 1
    for ingredient, amount in ingredients.items():
        context['recipe'][ingredient] = amount * servings
    return render(request, 'calculator/index.html', context)