from rest_framework import serializers, pagination
from .models import ProductTable

# class Product_serializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = ProductTable
#         fields=(
#             'name',
#             'price',
#             'ru_pname',
#
#
#         )
#         extra_kwargs = {
#             "trrate" : {
#                 "required" :False
#             }
#         }

class Product_serializer(serializers.Serializer):
    name = serializers.CharField(default=False)
    ru_pname = serializers.CharField(default=False)
    store = serializers.CharField(default=False)
    price = serializers.FloatField(default=False)
    trrate = serializers.FloatField(default=False)
    enrate = serializers.FloatField(default=False)
    rurate = serializers.FloatField(default=False)
    maxrate = serializers.FloatField(default=False)
    # class Meta:
    #     model = ProductTable
    #     fields=(
    #         'name',
    #         'price',
    #         'ru_pname',
    #         'trrate'
    #
    #
    #     )
