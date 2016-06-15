from . import models
def notifications_processor(request):
    notifications = models.Notification.objects.all().select_subclasses()
    print notifications.__dict__, "*"*80, "\nSIZE=", len(notifications)
    return {'notifications', notifications},
        
