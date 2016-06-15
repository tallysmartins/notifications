from django import template

register = template.Library()

@register.filter()
def show_notification_to(notification, user):
    print "AAAAaaaaaaaaaaa"*80, notification.show(user), notification.__class__
    return notification.show(user)
