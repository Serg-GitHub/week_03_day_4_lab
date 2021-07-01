from models.event import *


event1 = Event("2021/07/01", "Wedding", 100, "Ballroom", "Wedding of Mr & Mrs Smith", False)
event2 = Event("2021/07/01", "Birthday Party", 150, "Night Club", "Cameron's Birthday", False)
event3 = Event("2021/07/01", "Business Conference", 300, "Conference Hall", "Codeclan E50" , True)

events_list = [event1,event2,event3]

def add_new_event(event):
    events_list.append(event)
