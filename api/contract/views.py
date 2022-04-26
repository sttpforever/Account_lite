from rest_framework import viewsets
from rest_framework.decorators import action
from num2words import num2words
from django.http.response import HttpResponse
from docxtpl import DocxTemplate
from .models import Project, Customer, Bank, Check
from .serializers import (ProjectSerializer, CustomerSerializer,
                          BankSerializer, CheckSerializer)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        if serializer.is_valid:
            serializer.save(author=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(author=self.request.user)
        return owner_queryset


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        if serializer.is_valid:
            serializer.save(author=self.request.user)
    
    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(author=self.request.user)
        return owner_queryset


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(author=self.request.user)
        return owner_queryset


class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer

    def perform_create(self, serializer):
        if serializer.is_valid:
            serializer.save(author=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(author=self.request.user)
        return owner_queryset

    @action(detail=True)
    def download_check(self, request, pk):
        check = Check.objects.get(pk=pk)
        context = {}
        context['number'] = check.number
        context['project'] = ("Оплата за разработку" + " " +
                              Project.objects.get(pk=check.project.pk).description)
        context['bank_name'] = Bank.objects.get(pk=check.bank.pk)
        context['price'] = check.price
        context['fio'] = (check.author.last_name +
                          " " + check.author.first_name +
                          " " + check.author.fathers_name)
        context['address'] = (
            check.author.zip_code + ", " + check.author.city + ", " +
            check.author.street + " " + check.author.house + "- " +
            check.author.office)
        context['inn_user'] = check.author.inn
        context['payment_account'] = Bank.objects.get(pk=check.bank.pk).payment_account
        context['bik'] = Bank.objects.get(pk=check.bank.pk).bik
        context['correspondent_account'] = Bank.objects.get(pk=check.bank.pk).correspondent_account
        context['customer'] = check.project.customer.title
        context['price'] = check.price
        context['fio_short'] = (check.author.last_name + " " +
                                check.author.first_name[0] + "." +
                                check.author.fathers_name[0])
        context['date'] = check.create_date
        context['price_words'] = num2words(int(check.price), lang='ru')
        context['price_cent'] = (check.price - int(check.price))*100
        doc = DocxTemplate("word_tpl.docx")
        doc.render(context)
        file_name = f'счет {check.number}.docx'
        doc.save(file_name)
        response = HttpResponse(file_name, content_type='application/msword')
        response['Content-Disposition'] = (f'attachment;'
                                           f'filename={file_name}')
        return response
