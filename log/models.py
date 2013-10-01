from django.db import models

# Create your models here.

class Log(models.Model):
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=50)
    request_type = models.CharField(max_length=5)

    def __unicode__(self):
        return '%s - %s:%s' % (self.request_type, self.key, self.value)


