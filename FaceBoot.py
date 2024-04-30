try:
    import requests
    import os
    import glob
    import time
    import sys
    import json
    from google.cloud import storage
    from art import *
    from colorama import *

    init()
except ImportError:
    print("Librerias no Instaladas")
    print("")
    input("Press Enter For Install")
    import os
    os.system("pip install google-cloud-storage")
    os.system("pip install art")
    os.system("pip install colorama")


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
input(f"{azul}Press Enter Continue....")
os.system("python linux.py")
    

