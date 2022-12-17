from django.urls import path
from . import views
from .views import search_function_aux,search_function
app_name='product_app'

urlpatterns = [

    path('ser-search/<kword>',
         views.ProductSearchApiView.as_view(),
         name='ser-search'),

    path('search/',
         view=search_function_aux,
         name='search'),

    path('search_main/',
         view=search_function,
         name='search_main'),
]