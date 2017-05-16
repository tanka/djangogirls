from django.db import models
from datetime import datetime
from django.utils import timezone


class Tourgroup(models.Model):
    name = models.CharField(max_length=50)
    no_adults = models.IntegerField(default=0)
    no_children_below15 = models.IntegerField(default=0)
    no_children_below5 = models.IntegerField(default=0)
    entry_date = models.DateField('entry date')
    exit_date = models.DateField('exit date')
    itinerary_link = models.CharField(max_length=250)
    total_package_cost = models.FloatField(default=0.0)
    total_expense_assumed = models.FloatField(default=0.0)
    total_final_expense_incurred = models.FloatField(default=0.0)
    focal_person = models.CharField(max_length=50)
    focal_person_number = models.CharField(max_length=50)
    vehicle_no = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ', entry date - ' + self.entry_date.strftime('%d/%m/%Y') + ', focal person - ' + self.focal_person


class Guestcategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Guest(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=10)
    passport = models.CharField(max_length=50)
    permit_visa = models.CharField(max_length=50)
    passport_link = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    tourgroup = models.ForeignKey(Tourgroup, on_delete=models.CASCADE)
    Guestcategory = models.ForeignKey(Guestcategory)

    def __str__(self):
        return self.name + ' - nationality ' + self.nationality


class Expense(models.Model):
    date = models.DateField('expense date')
    particular = models.CharField(max_length=100)
    tds = models.FloatField(default=0.0)
    tpn = models.CharField(max_length=50)
    paid_for_service = models.FloatField(default=0.0)
    comment = models.CharField(max_length=250)
    tourgroup = models.ForeignKey(Tourgroup, on_delete=models.CASCADE)

    def __str__(self):
        return 'tds - ' + str(self.tds) + ' paid for service - ' + str(self.paid_for_service)


class People(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    idcardnumber = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    guide_license = models.CharField(max_length=50)
    driver_license = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' mobile - ' + self.mobile


class TourgroupPeople(models.Model):
    designation = models.CharField(max_length=20)
    people = models.ForeignKey(People)
    tourgroup = models.ForeignKey(Tourgroup)
from django.db import models

# Create your models here.
