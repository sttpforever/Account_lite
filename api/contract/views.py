from rest_framework import viewsets
from rest_framework.decorators import action
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
        context['project'] = Project.objects.get(pk=check.project.pk)
        context['bank'] = Bank.objects.get(pk=check.bank.pk)
        context['price'] = check.price
        doc = DocxTemplate("word_tpl.docx")
        doc.render(context)
        doc.save("generated_docx.docx")
