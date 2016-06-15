from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Notification(models.Model):
    active = models.IntegerField(default=1)
    unsubscribed_users = []
    color = models.CharField(max_length=10)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def factory(type):
        class WarningNotification(Notification):
            def show(self): pass

        class InformationNotification(Notification):
            def show(self): pass

        class DangerNotification(Notification):
            def show(self): pass

        class SuccessNotification(Notification):
            def show(self): pass

        class AdminNotification(Notification):
            def show(self): pass

        return eval(type + 'Notification()')
    factory = staticmethod(factory)
    
    class Meta:
        abstract = True

