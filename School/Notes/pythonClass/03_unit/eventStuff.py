import datetime

class Event:
    def __init__(self, Name, description, dateandtime):
        self.name, self.desc, self.datetime = Name, description, dateandtime

    def __str__(self):
        return f'{self.datetime.strftime("%b %d, %Y: %I:%M%p")} - {self.name}'

    def __lt__(self, other):
        obj1 = datetime.timedelta(self.datetime
bday = Event('Patricks Bday', '', datetime.datetime(2025, 2, 16))
print(bday)
