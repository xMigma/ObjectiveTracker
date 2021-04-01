import sys
from datetime import datetime
import pickle
import os
from pathlib import Path

path = os.path.dirname(__file__)
objetivos = {}

while True:
    respuesta = input(
        "Elige que quieres hacer:\n1. Añadir objetivo\n2. Ver objetivos pendientes\n3. Eliminar objetivo\n4. Salir\n")

    if respuesta == '1':
        nuevo_objetivo = input("\nInserta aquí el nombre del objetivo: ")

        # Asignamos a cada objetivo una hora de inicio
        hora_inicio = datetime.now()
        objetivos[nuevo_objetivo] = hora_inicio

        print("-----------------------------------------")
        print("Tu objetivo se ha añadido correctamente!")
        print("-----------------------------------------")

        # Guardamos el objetivo con su fecha de inicio en un archivo al que podremos acceder mas tarde
        with open(Path(path, "objetivos"), "wb") as f:
            pickle.dump(objetivos, f)
            f.close()

    if respuesta == '2':
       # Accedemos al archivo donde están almacenados los objetivos
        with open(Path(path, "objetivos"), "rb") as f:
            objetivos = pickle.load(f)

        print("")

        # Hacemos operaciones para devolverle al usuario cuanto tiempo ha transcurrido desde que inicio el objetivo
        for objetivo in objetivos:
            hora_actual = datetime.now()
            tiempo_transcurrido = hora_actual - objetivos[objetivo]
            dias, segundos = tiempo_transcurrido.days, tiempo_transcurrido.seconds
            horas = dias * 24 + segundos // 3600
            minutos = segundos % 3600 // 60
            segundos = segundos % 60

            print("- %s: %s dias %s:%s:%s" %
                  (objetivo, dias, horas, minutos, segundos))
        print("")

    if respuesta == '3':

        bandera = 1
        with open(Path(path, "objetivos"), "rb") as f:
            objetivos = pickle.load(f)

        print("Que objetivo quieres eliminar:")
        for objetivo in objetivos:
            print(str(bandera) + ". " + objetivo)
            bandera = bandera + 1
        print(str(bandera + 1) + ". Atrás")
        respuesta = input()

        for objetivo in list(objetivos):
            if respuesta == objetivo:
                objetivos.pop(objetivo)
                print("-----------------------------------------")
                print("El objetivo <<%s>> ha sido eliminado!" % objetivo)
                print("-----------------------------------------")
        
        # Guardamos el objetivo con su fecha de inicio en un archivo al que podremos acceder mas tarde
        with open(Path(path, "objetivos"), "wb") as f:
            pickle.dump(objetivos, f)
            f.close()


    if respuesta == '4':
        sys.exit()

    with open(Path(path, "objetivos"), "wb") as f:
        pickle.dump(objetivos, f)
        f.close()
    # Accedemos al archivo donde están almacenados los objetivos
    with open(Path(path, "objetivos"), "rb") as f:
        objetivos = pickle.load(f)