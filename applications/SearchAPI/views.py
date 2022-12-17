from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import ProductTable
from django.shortcuts import redirect,render, reverse
from django.http import JsonResponse
from django.core import serializers
import json
from rest_framework.generics import ListAPIView
from rest_framework import filters
from .serializers import Product_serializer
###########
import psycopg2
import pandas as pd
from difflib import SequenceMatcher
# Create your views here.



class ProductSearchApiView(ListAPIView):
    serializer_class = Product_serializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        #Get similar products using some word introduced by a user in the search line
        b=GetSimilarProds(kword,d)
        #Convert it do dicts:
        c = b.to_dict('records')
        #print(c)
        return c


class ProductTableOpen(ListAPIView):

    serializer_class = Product_serializer
    def get_queryset(self):
        #Here we get a queryset and convert it to dataframe and then dicts. Below we call it Once
        #launching a server, to avoid redirecting to DB every time
        a = ProductTable.objects.all().values()
        b = pd.DataFrame(list(a))
        c = b.to_dict('records')
        return c

'''Here we call our function as dataframe. So that it is called only
once without making request do DB as the user makes some search'''
d = ProductTableOpen().get_queryset()


#Here is a function that retrieves a keyword from a search line and redirects it
#to processing by ProductSearchApiView function
def search_function_aux(request):
    global d
    pstr = request.GET.get("search",'')

    if pstr:
        kword=pstr
        response = redirect(f"/ser-search/{kword}",ProductSearchApiView)
        return response


    return render(request, 'SearchAPI/Prod_Search.html')

###2 method:
'''It can be also implemented as a simple View-function, without serializers'''
def search_function(request):
    global d
    pstr = request.GET.get("search",'')

    if pstr:

        b=GetSimilarProds(pstr,d)
        #print(b)
        result = b.to_dict('records')
        print(result)
        return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii': False})

    return render(request, 'SearchAPI/Prod_Search.html')


'''Here are the functions that defines similarity and then sorts. They are called in 
the functions above while making a request'''
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def QuickSimilar(a, b):
    return SequenceMatcher(None, a, b).quick_ratio()

def GetSimilarProds(pstr,fn):

    for ar in fn:

        ar['trrate']=similar(ar["name"].lower(),pstr.lower())
        ar['enrate']=similar(ar["en_pname"].lower(),pstr.lower())
        ar['rurate']=similar(ar["ru_pname"].lower(),pstr.lower())
        ar['maxrate']=max( ar['trrate'],ar['enrate'],ar['rurate'])
    return pd.DataFrame(sorted(fn, reverse=True,key=lambda d: d['maxrate']))\
        [['name','ru_pname','price','store','trrate','enrate','rurate','maxrate']]

