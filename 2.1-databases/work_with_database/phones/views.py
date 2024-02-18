from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    user_actions = {'name': 'name',
                    'min_price': 'price',
                    'max_price': '-price'}

    phone_objects = Phone.objects.all()

    sort = request.GET.get('sort')
    if sort:
        phone_objects = Phone.objects.order_by(user_actions[sort])

    template = 'catalog.html'
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone_object}
    return render(request, template, context)
