from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Catalog, Seller
from .forms import AdvertForm


def index(request):
    catalog_objects_all = Catalog.objects.all()
    # sellers = Seller.objects.all()

    data_in_template_Index = {
        'catalogObjectsAll': catalog_objects_all , 
        'title': 'Список объявлений',
        # 'sellers': sellers,
        }
    return render(request, 'catalog\index.html', context=data_in_template_Index)

def get_seller(request, seller_id):
    catalog_filtred_in_IdSeller = Catalog.objects.filter(seller_id=seller_id)
    # sellers = Seller.objects.all()
    seller = Seller.objects.get(pk = seller_id)
    data_in_template_Sellers = {
        'catalogFiltredInIdSeller': catalog_filtred_in_IdSeller, 
        # 'sellers': sellers,
        'title': 'Фильтрация объявлений по Продавцам',
        'seller': seller,
        }
    return render(request, template_name = 'catalog/sellers.html', context=data_in_template_Sellers)

def view_advert(request, advert_id):
        # advert_item = Catalog.objects.get(pk=advert_id)
        advert_item = get_object_or_404(Catalog,pk=advert_id)
        data_in_template_ViewAdvert = {
        'advertItem': advert_item, 
        # 'title': 'Фильтрация объявлений по Продавцам',
        }
        return render(request, 'catalog/view_advert.html', context= data_in_template_ViewAdvert)

def add_advert(request):
    
    if request.method =='POST':
        form_advert = AdvertForm(request.POST)
        if form_advert.is_valid():
            print(form_advert.cleaned_data)
            Catalog.objects.create(**form_advert.cleaned_data)  # **- распаковка словаря
            return redirect('name_path_home')
    else:
        form_advert = AdvertForm()
    data_in_template_AddAdvert = {
        'formAdvert': form_advert,
    }
    return render(request, 'catalog/add_advert.html', context= data_in_template_AddAdvert)
