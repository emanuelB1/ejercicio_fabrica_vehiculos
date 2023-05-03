import platform
import os
import time
import cv2

def limpiar_pantalla(tiempo):
    time.sleep(tiempo)

    if platform.system() == "Windows":
        os.system("cls")

    else:
        os.system("clear")

def mostrar_imagenes():
    im = cv2.imread("diagramas/1.jpeg")

    cv2.imshow("diagrama", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
