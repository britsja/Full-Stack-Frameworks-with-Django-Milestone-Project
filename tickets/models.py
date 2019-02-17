from django.db import models
from django.contrib.auth.models import User

class Ticket_username(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Ticketcategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Ticket(models.Model):

    ticketusername = models.ForeignKey(User, on_delete=models.CASCADE)
    ticketname = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=False)
    category = models.ForeignKey(Ticketcategory,null=True, on_delete=models.CASCADE)
    created_date = models.DateField()
    status = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.ticketname

class Comments(models.Model):

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    commentusername = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=False)
    created_date = models.DateField()

    def __str__(self):
        return self.comment