from __future__ import unicode_literals
from model_utils.managers import InheritanceManager
from django.db import models

class Notification(models.Model):
    active = models.IntegerField(default=1)
    color = models.CharField(max_length=10)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    objects = InheritanceManager()

    def __str__(self):
        return "Message: " + self.message

    def factory(type):
        return eval(type + 'Notification()')
    factory = staticmethod(factory)

    class Meta:
        abstract = False
    
class WarningNotification(Notification):
    def show(self, user):
        return True
    def css(self):
        return "warning-notification"

class InformationNotification(Notification):
    def show(self, user):
        return True
    def css(self):
        return "information-notification"

class UnloggedUserNotification(Notification):
    def show(self, user):
        return user.is_anonymous()
    def css(self):
        return "unloggeduser-notification"

class AdminNotification(Notification):
    def show(self, user):
        return user.is_superuser
    def css(self):
        return "admin-notification"


