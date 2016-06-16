from __future__ import unicode_literals
from model_utils.managers import InheritanceManager
from django.db import models
from .dispatch import Publisher

class Notification(models.Model, Publisher):
    active = models.IntegerField(default=1)
    color = models.CharField(max_length=10)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    type = "NOTIFICATION"
    objects = InheritanceManager()

    def __str__(self):
        return "Message: " + self.message

    @classmethod
    def factory(cls, type):
        new_notification = eval(type + 'Notification()')
        cls.publish(new_notification.type)
        return new_notification

    class Meta:
        abstract = False
    
class WarningNotification(Notification):
    type = "WARNING_NOTIFICATION"

    def show(self, user):
        return True
    def css(self):
        return "warning-notification"

class InformationNotification(Notification):
    type = "INFORMATION_NOTIFICATION"

    def show(self, user):
        return True
    def css(self):
        return "information-notification"

class UnloggedUserNotification(Notification):
    type = "UNLOGGED_NOTIFICATION"

    def show(self, user):
        return user.is_anonymous()
    def css(self):
        return "unloggeduser-notification"

class AdminNotification(Notification):
    type = "ADMIN_NOTIFICATION"

    def show(self, user):
        return user.is_superuser
    def css(self):
        return "admin-notification"


