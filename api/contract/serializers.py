from rest_framework import serializers
from .models import Project, Customer, Bank, Check


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'contract_number', 'description', 'customer',
                  'price', 'additional_pay', 'total_price', 'pk', 'dohod',
                  'last_piece')
        model = Project


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'description', 'pk')
        model = Customer


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'pk')
        model = Bank


class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('number', 'project', 'bank', 'price', 'pk')
        model = Check
