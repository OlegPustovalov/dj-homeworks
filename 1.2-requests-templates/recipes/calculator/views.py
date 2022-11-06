#from django.conf import setting

from django.shortcuts import render, reverse

from django.http import HttpResponse



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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def home_view(request):
    
    template_name = 'calculator/home.html'
    pages = {
        'Cостав для омлета': reverse('omlet'),
        'Состав для пасты': reverse('pasta'),
        'Cостав для бутерброда': reverse('buter'),
    }
    context = {
        'pages': pages
    }
    return render(request,template_name, context)

def omlet_view(request):   
    N = int(request.GET.get("servings",1))
    DATA1 = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    }   
    }
    i=0
    st1 =''
    for st1 in DATA1:
        for i in DATA1[st1]:
            DATA1[st1][i]= DATA1[st1][i]*N
    context = DATA1
    return render(request, 'calculator/omlet.html', context)

def pasta_view(request):
    N = int(request.GET.get("servings",1))
    DATA1 = {
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    }
    }
    i=0
    st1 =''
    for st1 in DATA1:
        for i in DATA1[st1]:
            DATA1[st1][i]= DATA1[st1][i]*N
    context = DATA1
    return render(request, 'calculator/pasta.html', context)

def buter_view(request):
    N = int(request.GET.get("servings",1))
    DATA1 = {
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
    }
    i=0
    st1 =''
    for st1 in DATA1:
        for i in DATA1[st1]:
            DATA1[st1][i]= DATA1[st1][i]*N
    context = DATA1
    return render(request,'calculator/burger.html', context)

def omlet_many_view(request,param1):
   N=param1
   DATA1 = DATA
   for st1 in DATA1:
        for i in DATA1[st1]:
            DATA1[st1][i]= DATA1[st1][i]*N
   context = DATA1
   return render(request, 'calculator/omlet.html', context)

def pasta_many_view(request,param2):
   N=param2
   DATA1 = DATA
   for st1 in DATA1:
        for i in DATA1[st1]:
            DATA1[st1][i]= DATA1[st1][i]*N
   context = DATA1
   return render(request, 'calculator/pasta.html', context)
   
def buter_many_view(request,param3):
   N=param3
   DATA1 = DATA
   for st1 in DATA1:
        for i in DATA1[st1]:
            DATA1[st1][i]= DATA1[st1][i]*N
   context = DATA1
   return render(request, 'calculator/burger.html', context)   
   
   raise NotImplemented