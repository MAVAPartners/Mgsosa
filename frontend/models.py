from django.db import models

# Create your models here.


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    createdOn.editable = False
    fromDate = models.DateTimeField()
    toDate = models.DateTimeField()


class EventImage(models.Model):
    id = models.AutoField(primary_key=True)
    eventId = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    imageUrl = models.ImageField()
