#Creditos: XONIDU

from pyautogui import write, press
from time import sleep

opt: int  # option, se coloca en str para evitar problemas de sintaxis

def spam_n():
    msj: str = input("\nMensaje: ")
    num: int = int(input("Cantidad de mensajes: "))
    print("Iniciando en 3 segundos...")

    sleep(3)  # Dar un momento para iniciar el spam

    for i in range(num):
        write(msj)
        press("enter")
    print("SPAM finalizado UwU")

def spam_t():
    ruta = input("\nRuta del archivo .txt: ")

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.split()  # Divide por palabras
            print(f"Se encontraron {len(palabras)} palabras. Iniciando en 3 segundos...")
            sleep(3)

            for palabra in palabras:
                write(palabra)
                press("enter")
            print("SPAM de texto finalizado UwU")

    except FileNotFoundError:
        print("Archivo no encontrado")

#Para mas contenido, buscanos como: xonidu

while True:
    print(chr(27) + f"[1;31m" + "")
    print("""-xonispam-
▒▒▒▄▄▄▄▄▒▒▒
▒▄█▄█▄█▄█▄▒
▒▒▒▒░░░▒▒▒▒
▒▒▒▒░░░▒▒▒▒
▒▒▒▒░░░▒▒▒▒
""")

    print("""\nSPAM normal   [0]
SPAM de texto [1]
SALIR         [2]\n""")
    opt = input("Opcion: ")

    if opt == "0":
        spam_n()
    elif opt == "1":
        spam_t()
    elif opt == "2":
        print("Adios :3")
        break
    else:
        print("Opcion invalida\n")
