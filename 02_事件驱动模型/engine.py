#-*- coding=utf-8 -*-
from event_manager import EventManager, Timer

def start_fund():
    print("start fund... ")

def start_extreme():
    print("start extreme... ")

class Event_Source():
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def start(self):
        event_name = "Fund"
        self.event_manager.SendEvent(event_name)

class Listener():
    def __init__(self, event_name, func):
        self.event_name = event_name
        self.processor = func

def test():
    event_name = ["Fund", "Extreme"]
    listener = [
        Listener(event_name[0],start_fund),
        Listener(event_name[1],start_extreme)
    ]

    event_manager = EventManager()
    event_manager.AddEventListener(listener[0])
    
    event_driver = Event_Source(event_manager)

    event_driver.start() 
    event_driver.start() 
    event_driver.start() 

    event_manager.Start()

#   listener[0].processor()

#   return event_name, listener, event_manager, event_driver
    
if __name__=="__main__":
    test()
