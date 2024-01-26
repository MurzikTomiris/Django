from django.shortcuts import render


def index(request):
    title = 'Главная'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

def about(request):
    title = 'О нас'

    context = {
        'title': title,
    }

    return render(request, 'about.html', context)

def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
    }

    return render(request, 'contacts.html', context)

def product(request):
    title = 'Товары'

    context = {
        'title': title,
    }

    return render(request, 'product.html', context)

def products(request):
    title = 'Продукт'

    context = {
        'title': title,
    }

    return render(request, 'products.html', context)
