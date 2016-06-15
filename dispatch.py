from collections import defaultdict


messages_pool = defaultdict(list)


class Publisher():
    global messages_pool
    def publish(message_type, *args, **kwargs):
        for callback in messages_pool[message_type]:
            callback(*args, **kwargs) 
  

class Subscriber():
    global messages_pool
    def subscribe(message_type, callback):
        messages_pool[message_type].append(callback)

    def unsubscribe(message_type, callback):
        if callback in messages_pool[message_type]:
            messages_pool[message_type].remove(callback)
