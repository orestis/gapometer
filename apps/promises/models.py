from django.db import models

from tagging.fields import TagField

# Create your models here.

class Status(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Promise(models.Model):

    title = models.CharField(max_length=400)
    number = models.PositiveIntegerField()
    body = models.TextField()
    date_promised = models.DateTimeField()

    status = models.ForeignKey(Status)
    tags = TagField()

    @models.permalink
    def get_absolute_url(self):
        return ("promise_detail", [self.pk])


    @property
    def hashtag(self):
        return "#km%d" % self.number
    

    def __unicode__(self):
        return self.title



class Update(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    promise = models.ForeignKey(Promise, related_name="updates")

    def __unicode__(self):
        return self.title


