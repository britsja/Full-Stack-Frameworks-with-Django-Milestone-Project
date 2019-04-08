from django.db import models
from features.models import Features

class Order(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    country = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=False)
    county_state = models.CharField(max_length=50, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.name)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    feature = models.ForeignKey(Features, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    def __str__(self):
        return "{0} thousand votes for feature titled '{1}' at ${2} per thousand".format(self.quantity, self.feature.featurename, 0.1)
