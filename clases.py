import csv
import random
from funciones_utilitarias import *




class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
    
    def guardar_datos_csv_globales(self, instancia, nombre):
        archivo = open("vehiculos.csv", "a")
        datos = [(nombre + ".csv", instancia.__class__, instancia.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()
        print("Añadiendo el Vehiculo al archivo: vehiculos.csv")
        limpiar_pantalla(4)

    def guardar_datos_csv(self, instancia, nombre):
        archivo = open("instancias_creadas/" + nombre + ".csv", "w")
        datos = [(instancia.__class__, instancia.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()
        print(f"Guardando los datos del Vehiculo en un archivo individual, en la carpeta: instancias_creadas, con el nombre: {nombre}.csv")
        limpiar_pantalla(4)
    
    def leer_datos_cvs(self, nombre):
        archivo = open("instancias_creadas/" + nombre + ".csv", "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            if len(vehiculo) != 0:
                print("Se ha generado el registro del objeto")
                print(vehiculo)
        archivo.close()
        limpiar_pantalla(5)
        
        

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc"
    
    def guardar_datos_csv_automovil(self, instancia, nombre):
        archivo = open("clase_automovil.csv", "a")
        datos = [(nombre + ".csv", instancia.__class__, instancia.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()
        print("Añadiendo el Vehiculo al archivo: clase_automovil.csv")
        limpiar_pantalla(4)
    
    



class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc, numero de puestos: {self.numero_puestos}"
    
    def guardar_datos_csv_particular(self, instancia, nombre):
        archivo = open("clase_particular.csv", "a")
        datos = [(nombre + ".csv", instancia.__class__, instancia.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()
        print("Añadiendo el Vehiculo al archivo: clase_particular.csv")
        limpiar_pantalla(4)
    
class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc, Carga: {self.carga} Kg"
    
    def guardar_datos_csv_carga(self, instancia, nombre):
        archivo = open("clase_carga.csv", "a")
        datos = [(nombre + ".csv", instancia.__class__, instancia.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()
        print("Añadiendo el Vehiculo al archivo: clase_carga.csv")
        limpiar_pantalla(4)
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Tipo: {self.tipo}"
    
    def guardar_datos_csv_bicicleta(self, instancia, nombre):
        archivo = open("clase_bicicleta.csv", "a")
        datos = [(nombre + ".csv", instancia.__class__, instancia.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()
        print("Añadiendo el Vehiculo al archivo: clase_bicicleta.csv")
        limpiar_pantalla(4)

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, nmro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.nmro_radios = nmro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nmro_radios}"
    
    def guardar_datos_csv_motocicleta(self, instancia, nombre):
        archivo = open("clase_motocicleta.csv", "a")
        datos = [(nombre + ".csv", instancia.__class__, instancia.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()
        print("Añadiendo el Vehiculo al archivo: clase_motocicleta.csv")
        limpiar_pantalla(4)