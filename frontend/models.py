from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    image = models.FileField(blank=True)
    createdOn.editable = False
    fromDate = models.DateTimeField()
    toDate = models.DateTimeField()
    
    def __str__(self):
        return self.name

def get_image_filename(instance, filename):
    title = instance.event.name
    slug = slugify(title)
    return "event_images/%s-%s" % (slug, filename)

class EventImage(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

    def __str__(self):
        return self.event.name
