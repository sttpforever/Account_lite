from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Project(models.Model):
    title = models.CharField('Имя', max_length=200)
    contract_number = models.CharField('Номер договора', max_length=200)
    description = models.TextField()
    create_date = models.DateTimeField("date published",
                                       auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name="projects")
    customer = models.ForeignKey('Customer',
                                 on_delete=models.PROTECT,
                                 related_name="projects")
    price = models.FloatField('Стоимость проекта')
    additional_pay = models.FloatField('Дополнительная оплата',
                                       default=0)

    def total_price(self):
        return self.price + self.additional_pay

    def dohod(self):
        return (self.price + self.additional_pay)*0.9
    
    def last_piece(self):
        return (self.price + self.additional_pay)*0.1

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.title[:15]


class Customer(models.Model):
    title = models.CharField('Имя', max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name="customers")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title[:15]


class Bank(models.Model):
    name = models.CharField('название банка', max_length=200)

    def __str__(self):
        return str(self.name)


class Check(models.Model):
    number = models.CharField('номер счета', max_length=200)
    project = models.ForeignKey('Project',
                                on_delete=models.PROTECT,
                                related_name="checks")
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT,
                             related_name='checks')
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name="checks")
    price = models.FloatField('Стоимость счета')

    class Meta:
        ordering = ['-bank', "-number"]

    def __str__(self):
        return str(self.number)
