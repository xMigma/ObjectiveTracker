import sys
from datetime import datetime
import json
import os
from pathlib import Path
from dateutil import parser

path = os.path.dirname(__file__)
with open("objectives.json") as f:
    json_data = json.load(f)
    objectives = json_data["objectives"]    

while True:
    answer = input(
        "Elige que quieres hacer:\n1. Añadir objetivo\n2. Ver objetivos pendientes\n3. Eliminar objetivo\n4. Salir\n")

    if answer == '1':

        name = input("\nInserta aquí el nombre del objetivo: ")
        start_date = str(datetime.now())
        objectives.append({"name": name, "start_date": start_date})

        print("-----------------------------------------")
        print("Tu objetivo se ha añadido correctamente!")
        print("-----------------------------------------")

        with open(Path(path, "objectives.json"), "w") as f:
            json.dump(json_data, f,  indent=2)
            f.close()

    if answer == '2':
       # Accedemos al archivo donde están almacenados los objetivos
        with open(Path(path, "objectives.json")) as f:
            json_data = json.load(f)
            objectives = json_data["objectives"]    

        print("")

        # Hacemos operaciones para devolverle al usuario cuanto tiempo ha transcurrido desde que inicio el objetivo
        for objective in objectives:
            start_date = parser.parse(objective["start_date"])
            hora_actual = datetime.now()
            tiempo_transcurrido = hora_actual - start_date
            dias, segundos = tiempo_transcurrido.days, tiempo_transcurrido.seconds
            horas = dias * 24 + segundos // 3600
            minutos = segundos % 3600 // 60
            segundos = segundos % 60

            print("- %s: %s dias %s:%s:%s" %
                  (objective["name"], dias, horas, minutos, segundos))
        print("")

    if answer == '3':

        bandera = 1
        with open(Path(path, "objectives.json"), "r") as f:
            json_data = json.load(f)
            objectives = json_data["objectives"]

        print("Que objetivo quieres eliminar:")
        for objective in objectives:
            print(str(bandera) + ". " + str(objective['name']))
            bandera = bandera + 1

        print(str(bandera) + ". Atrás")
        answer = input()

        bandera = 0
        for i in objectives:
            print(objectives)
            if int(answer) == bandera + 1:
                deleted_objective = objectives[bandera]["name"]
                del objectives[bandera]
                        
                print("-----------------------------------------")
                print("El objetivo <<%s>> ha sido eliminado!" % deleted_objective) 
                print("-----------------------------------------")
            ++bandera   
                
        # Guardamos el objetivo con su fecha de inicio en un archivo al que podremos acceder mas tarde
        with open(Path(path, "objectives.json"), "w") as f:
            json.dump(json_data, f,  indent=2)
            f.close()

    if answer == '4':
        sys.exit()