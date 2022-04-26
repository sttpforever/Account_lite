from rest_framework import serializers
from .models import Project, Customer, Bank, Check


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['author']
        model = Project


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['author']
        model = Customer


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['author']
        model = Bank


class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['author']
        model = Check
