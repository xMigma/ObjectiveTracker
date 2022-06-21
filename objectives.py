import json
import parser
from datetime import datetime
from dateutil import parser

class Objectives:
    def __init__(self):
        with open("objectives.json", "r") as f:
            json_data = json.load(f)
        self.json_data = json_data

    def open_json(self):
        return self.json_data

    def close_json(self, json_data):
        with open("objectives.json", "w") as f:
            json.dump(json_data, f,  indent=2)
            f.close()

    def obtain_date(self, objectives):
        for self.objective in objectives:
            self.start_date = parser.parse(self.objective["start_date"])
            self.actual_date = datetime.now()         
            self.time_elapsed = self.actual_date - self.start_date
            self.days, self.seconds = self.time_elapsed.days, self.time_elapsed.seconds
            self.hours =self.days * 24 + self.seconds // 3600
            self.minutos = self.seconds % 3600 // 60
            self.seconds = self.seconds % 60

            print ("- %s: %s dias %s:%s:%s" % (self.objective["name"], self.days, self.hours, self.minutos, self.seconds))
