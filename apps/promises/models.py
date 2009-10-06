from django.db import models

# Create your models here.

class Status(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Source(models.Model):
    title = models.CharField(max_length=400)
    link = models.CharField(max_length=400)

    def __unicode__(self):
        return self.title



class Promise(models.Model):

    title = models.CharField(max_length=400)
    body = models.TextField()

    status = models.ForeignKey(Status)
    source = models.ManyToManyField(Source)

    def __unicode__(self):
        return self.title


