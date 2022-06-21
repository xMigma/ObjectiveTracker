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
            self.hora_actual = datetime.now()         
            self.tiempo_transcurrido = self.hora_actual - self.start_date
            self.dias, self.segundos = self.tiempo_transcurrido.days, self.tiempo_transcurrido.seconds
            self.horas =self.dias * 24 + self.segundos // 3600
            self.minutos = self.segundos % 3600 // 60
            self.segundos = self.segundos % 60

            print ("- %s: %s dias %s:%s:%s" % (self.objective["name"], self.dias, self.horas, self.minutos, self.segundos))
