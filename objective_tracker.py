import sys
import os
from objectives import Objectives
from datetime import datetime


while True:

    json_data = Objectives().open_json()
    objectives = json_data["objectives"]
    answer = input("Elige que quieres hacer:\n1. Añadir objetivo\n2. Ver objetivos pendientes\n3. Eliminar objetivo\n4. Salir\n")

    if answer == '1':
        name = input("\nInserta aquí el nombre del objetivo: ")
        start_date = str(datetime.now())
        objectives.append({"name": name, "start_date": start_date})

        print("-----------------------------------------")
        print("Tu objetivo se ha añadido correctamente!")
        print("-----------------------------------------")
    if answer == '2':
        Objectives().obtain_date(objectives)
    if answer == '3':
        print("Que objetivo quieres eliminar:")
        bandera = 1

        for objective in objectives:
            print(str(bandera) + ". " + str(objective['name']))
            bandera = bandera + 1

        answer = input(str(bandera) + ". Atrás\n")
        bandera = 0

        for i in objectives:
            if int(answer) == bandera + 1:
                deleted_objective = objectives[bandera]["name"]
                del objectives[bandera]                      
                print("-----------------------------------------")
                print("El objetivo <<%s>> ha sido eliminado!" % deleted_objective) 
                print("-----------------------------------------")
            ++bandera   

    if answer == '4':
        sys.exit()

    Objectives().close_json(json_data)      