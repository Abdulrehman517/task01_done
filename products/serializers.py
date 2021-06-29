from django.db import models
from django.db.models import fields
# from rest_framework.fields import ReadOnlyField
from .models import Product, Variant
from rest_framework import serializers


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, source="prod_var")

    class Meta:
        model = Product
        fields = '__all__'
