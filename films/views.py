from django.shortcuts import render, redirect
from .models import *
from .form import *


# Create your views here.
def index(req):
    return render(req, 'index.html')


def forma1(req):
    bd = Movie.objects.all()
    data = {'database': bd}
    return render(req, 'all_films.html', context=data)


def forma2(req):
    if req.POST:
        # показываем, что не заполнено, если нажали отправить, а форма не заполнена
        country_filter = FilterCountry(req.POST)
        if country_filter.is_valid():
            print('ok')
            k1 = country_filter.cleaned_data.get('country')
            print(k1)
            bd = Movie.objects.filter(country=k1)
            data = {'database': bd}
            return render(req, 'all_films.html', context=data)
        else:
            print('neok')

    else:
        country_filter = FilterCountry()
    data = {'form2': country_filter}
    return render(req, "filter_country.html", context=data)


def forma3(req):
    if req.POST:
        year_filter = FilterYear(req.POST)
        if year_filter.is_valid():
            print('ok')
            k2 = year_filter.cleaned_data.get('year')
            print(k2)
            bd = Movie.objects.filter(year=k2)
            data = {'database': bd}
            return render(req, 'all_films.html', context=data)
        else:
            print('neok')
    else:
        year_filter = FilterYear()
    data = {'form3': year_filter}
    return render(req, 'filter_year.html', context=data)


def forma4(req):
    if req.POST:
        double_filter = DoubleFilter(req.POST)
        if double_filter.is_valid():
            print('ok')
            k1 = double_filter.cleaned_data.get('country')
            k2 = double_filter.cleaned_data.get('year')
            print(k1, k2)
            bd = Movie.objects.filter(country=k1).exclude(year=k2)
            data = {'database': bd}
            return render(req, 'all_films.html', context=data)
        else:
            print('neok')
    else:
        double_filter = DoubleFilter()
    data = {'form4': double_filter}
    return render(req, 'country_wihout_year.html', context=data)
