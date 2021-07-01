class Event():

    def __init__(self, date, event_name, guest_total, room_location, description,recurring ):
        self.date = date
        self.name = event_name
        self.guests = guest_total
        self.room = room_location
        self.description = description
        self.recurring = recurring

    