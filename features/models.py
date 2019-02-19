from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Features(models.Model):

    featureusername = models.ForeignKey(User, on_delete=models.CASCADE)
    featurename = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(blank=False, default=False)
    upvotes = models.IntegerField()
    closed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.featurename

class FeatureComments(models.Model):

    feature = models.ForeignKey(Features, on_delete=models.CASCADE)
    commentusername = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.comment