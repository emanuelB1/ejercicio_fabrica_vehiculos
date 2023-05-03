from clases import *



def menu():
    opcion = ""
    while opcion not in range(1, 6) and opcion != 5:
        try:
            print("Fabrica de Vehiculos")
            print("1 - Crear Vehiculos")
            print("2 - Leer el Registro de Vehiculos")
            print("3 - Mostrar el Diagrama de Clases de este programa")
            print("4 - Leer Tutorial")
            print("5 - Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                limpiar_pantalla(0.5)
                opcion = "" 
                while opcion not in range(1, 5):
                    try:
                        print("Que tipo de Vehiculo desea crear")
                        print("1 - Automovil")    
                        print("2 - Automovil Particular")  
                        print("3 - Automovil de Carga")  
                        print("4 - Bicicleta")  
                        print("5 - Motocicletas") 
                        print("6 - Salir") 
                        opcion = int(input("Ingrese una opcion: "))
                        if opcion == 1:
                            limpiar_pantalla(0.5)
                            crear_automvil()
                            opcion = ""

                        elif opcion == 2:
                            limpiar_pantalla(0.5)
                            crear_particular()
                            opcion = ""

                        elif opcion == 3:
                            limpiar_pantalla(0.5)
                            crear_carga()
                            opcion = ""

                        elif opcion == 4:
                            limpiar_pantalla(0.5)
                            crear_bicicleta()
                            opcion = ""

                        elif opcion == 5:
                            limpiar_pantalla(0.5)
                            crear_motocileta()
                            opcion = ""

                        elif opcion == 6:
                            limpiar_pantalla(0.5)
                            opcion = ""
                            break
                    except ValueError:
                        limpiar_pantalla(0.5)
                        print("Ingrese una opcion valida")
                        limpiar_pantalla(1)
                        
            
            elif opcion == 2:
                limpiar_pantalla(0.5) 
                nombre = ""
                while nombre == "" or nombre != "7":
                    print("Registro de Vehiculos")
                    print("1 - Leer Registro de todos los Vehiculos")
                    print("2 - Leer Registro de los Vehiculos de Clase Automovil")
                    print("3 - Leer Registro de los Vehiculos de Clase Particular")
                    print("4 - Leer Registro de los Vehiculos de Clase Carga")
                    print("5 - Leer Registro de los Vehiculos de Clase Bicicleta")
                    print("6 - Leer Registro de los Vehiculos de Clase Motocicleta")
                    print("7 - Salir")
                    if nombre == "7":
                        limpiar_pantalla(0.5)
                    try:
                        nombre = input("Ingrese una opcion: ").lower()
                        if nombre == "1":
                            leer_datos_csv("vehiculos.csv", "de todas las Clases")
                        
                        elif nombre == "2":
                            leer_datos_csv("clase_automovil.csv", "de clase Automovil")

                        elif nombre == "3":
                            leer_datos_csv("clase_particular.csv", "de clase Particular")

                        elif nombre == "4":
                            leer_datos_csv("clase_carga.csv", "de clase Carga")

                        elif nombre == "5":
                            leer_datos_csv("clase_bicicleta.csv", "de clase Bicicleta")

                        elif nombre == "6":
                            leer_datos_csv("clase_motocicleta.csv", "de clase Motocicleta")
                        
                        elif nombre == "salir":
                            nombre = "7"
                            limpiar_pantalla(0.5)
                        opcion = ""
                    except:
                        opcion = ""
                limpiar_pantalla(0.5)
            
            elif opcion == 3:
                try:
                    limpiar_pantalla(0.5)
                    opcion = ""
                    print("Se abrira una ventana mostrando el diagrama de Clases")
                    limpiar_pantalla(3)
                    print("para cerrar esta ventana pulse una tecla")
                    mostrar_imagenes()
                    limpiar_pantalla(0.5)
                    opcion = ""
                except:
                    opcion = ""

            elif opcion == 4:
                limpiar_pantalla(0.5)
                salir = ""
                while salir == "" or salir != "4":
                    print("Tutorial")
                    print("1 - Frabricacion de Vehiculos y Gestion de Registros")
                    print("2 - Lectura de Registros")
                    print("3 - Visualizacion de Diagramas")
                    print("4 - Salir")
                    salir = input("Ingrese una opcion: ")
                    limpiar_pantalla(0.5)

                    if salir == "1":
                        print("*****      Frabricacion de Vehiculos y Gestion de Registros     ********")
                        print("Puede Frabricar Vehiculos de diversas clases en la opcion 1.")
                        print("Estos Vehiculos se registraran en documentos csv.")
                        print("Se generara un documento general, es decir de todos los Vehiculos, uno por Clases y uno individual.")
                        print("Tanto el documento general como los por clases, se alojaran la carpeta principal.")
                        print("Los documentos Individuales se alojaran en la carpeta: instancias_creadas")
                        print("Puede borra los registros existences, pero ya no podra leerlos.")
                        print("Al Fabricar un nuevo Vehiculos se generaran los documentos correspondientes.")
                        print("En caso de que estos documentos no existan se crearan.")
                        print("Si ya existen los nuevos Vehiculos se añadiran en la siguiente linea del documento")
                        print("Los documentos individuales siempre se crean y son unicos e irrepetibles")

                    if salir == "2":
                        print("*****                Lectura de Registros               ********")
                        print("Puede Leer los registros generados en la opcion: 2, siempre y cuando ya existan.")
                        print("Si no existen, tendra que crear un Vehiculo para generar un registro.")
                       
                    elif salir == "3":
                        print("*****              Visualizacion de Diagramas            ********")
                        print("Puede ver los Diagramas que se usaron para crear este programa en la opcion: 3.")
                        print("Esto abrira una ventana emergente la cual, se podra cerrar pulsando cualquier tecla.")
                        
                opcion = ""
                

                
                

        except ValueError:
            limpiar_pantalla(0.5)
            print("Ingrese una opcion valida")
            limpiar_pantalla(1)
            


            
def crear_automvil():
    lista_vehiculos = []
    opcion = ""
    while type(opcion) != int:
    
        try:
            opcion = int(input("Cuantos Vehiculos desea insertar: "))
            
                
        except ValueError:
            print("Ingrese un numero valido")

    contador = 0
    while contador != opcion:
        numero_ruedas = ""
        velocidad = ""
        cilindrada = ""

        
        marca = input("Inserte la Marca del de Automovil: ")
        modelo = input("Inserte el Modelo: ")
        while type(numero_ruedas) != int:
            try:
                numero_ruedas = int(input("Inserte el Numero de Ruedas: "))
            except ValueError:
                print("Ingrese un numero valido")

        while type(velocidad) != int:
            try:
                velocidad = int(input("Inserte la Velocidad en km/h: "))
            except ValueError:
                print("Ingrese un numero valido")
        
        while type(cilindrada) != int:
            try:
                cilindrada = int(input("Inserte el Cilindraje cc: "))
            except ValueError:
                print("Ingrese un numero valido")
        limpiar_pantalla(1)            
        instancia = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
        limpiar_pantalla(1)
        nombre = random.randint(1, 1000)
        nombre = str(nombre)
        instancia.guardar_datos_csv(instancia, nombre)
        instancia.guardar_datos_csv_automovil(instancia, nombre)
        instancia.guardar_datos_csv_globales(instancia, nombre)
        instancia.leer_datos_cvs(nombre)
        lista_vehiculos.append(instancia)
        contador += 1
            
    
        
    verificar_instancias(lista_vehiculos)
    



def crear_particular():
    lista_particulares = []
    opcion = ""
    while type(opcion) != int:
    
        try:
            opcion = int(input("Cuantos Vehiculos Particulares desea insertar: "))
            
                
        except ValueError:
            print("Ingrese un numero valido")

    contador = 0
    while contador != opcion:
        numero_ruedas = ""
        velocidad = ""
        cilindrada = ""
        numero_puestos = ""

        
        marca = input("Inserte la Marca del de Automovil: ")
        modelo = input("Inserte el Modelo: ")
        while type(numero_ruedas) != int:
            try:
                numero_ruedas = int(input("Inserte el Numero de Ruedas: "))
            except ValueError:
                print("Ingrese un numero valido")

        while type(velocidad) != int:
            try:
                velocidad = int(input("Inserte la Velocidad en km/h: "))
            except ValueError:
                print("Ingrese un numero valido")
        
        while type(cilindrada) != int:
            try:
                cilindrada = int(input("Inserte el Cilindraje cc: "))
            except ValueError:
                print("Ingrese un numero valido")

        while type(numero_puestos) != int:
            try:
                numero_puestos = int(input("Inserte el Numero de Puestos: "))
            except ValueError:
                print("Ingrese un numero valido")
        limpiar_pantalla(1)
        instancia = Particular(marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos)
        limpiar_pantalla(1)
        nombre = random.randint(1, 1000)
        nombre = str(nombre)
        instancia.guardar_datos_csv(instancia, nombre)
        instancia.guardar_datos_csv_particular(instancia, nombre)
        instancia.guardar_datos_csv_globales(instancia, nombre)
        instancia.leer_datos_cvs(nombre)
        lista_particulares.append(instancia)
        contador += 1
            
    
        
    verificar_instancias(lista_particulares)




def crear_carga():


    lista_carga = []
    opcion = ""
    while type(opcion) != int:
    
        try:
            opcion = int(input("Cuantos Vehiculos de Carga desea insertar: "))
            
                
        except ValueError:
            print("Ingrese un numero valido")

    contador = 0
    while contador != opcion:
        numero_ruedas = ""
        velocidad = ""
        cilindrada = ""
        carga = ""

        
        marca = input("Inserte la Marca del de Automovil de Carga: ")
        modelo = input("Inserte el Modelo: ")
        while type(numero_ruedas) != int:
            try:
                numero_ruedas = int(input("Inserte el Numero de Ruedas: "))
            except ValueError:
                print("Ingrese un numero valido")

        while type(velocidad) != int:
            try:
                velocidad = int(input("Inserte la Velocidad en km/h: "))
            except ValueError:
                print("Ingrese un numero valido")
        
        while type(cilindrada) != int:
            try:
                cilindrada = int(input("Inserte el Cilindraje cc: "))
            except ValueError:
                print("Ingrese un numero valido")

        while type(carga) != int:
            try:
                carga = int(input("Inserte el maximo de Carga en Kg: "))
            except ValueError:
                print("Ingrese un numero valido")
        limpiar_pantalla(1)          
        instancia = Carga(marca, modelo, numero_ruedas, velocidad, cilindrada, carga)
        limpiar_pantalla(1)
        nombre = random.randint(1, 1000)
        nombre = str(nombre)
        instancia.guardar_datos_csv(instancia, nombre)
        instancia.guardar_datos_csv_carga(instancia, nombre)
        instancia.guardar_datos_csv_globales(instancia, nombre)
        instancia.leer_datos_cvs(nombre)
        lista_carga.append(instancia)
        contador += 1
            
    
        
    verificar_instancias(lista_carga)




def crear_bicicleta():
    lista_bicicletas = []
    opcion = ""
    while type(opcion) != int:
    
        try:
            opcion = int(input("Cuantas Bicicletas desea insertar: "))
            
                
        except ValueError:
            print("Ingrese un numero valido")

    contador = 0
    while contador != opcion:
        numero_ruedas = ""
        tipos = ["Urbana", "Carrera", "1", "2"]
        tipo = ""
        

        
        marca = input("Inserte la Marca de la Bicicleta: ")
        modelo = input("Inserte el Modelo: ")
        while type(numero_ruedas) != int:
            try:
                numero_ruedas = int(input("Inserte el Numero de Ruedas: "))
            except ValueError:
                print("Ingrese un numero valido")
        
        while tipo not in tipos:
            try:
                print("Inserte un tipo de Bicicleta\n1 - Urbana\n2 - Carrera")
                tipo = input("tipo: ").capitalize()
                if tipo == "1":
                    tipo = "Urbana"
                elif tipo == "2":
                    tipo = "Carrera"

            except:
                pass
        

       
        limpiar_pantalla(1)
        instancia = Bicicleta(marca, modelo, numero_ruedas, tipo)
        limpiar_pantalla(1)
        nombre = random.randint(1, 1000)
        nombre = str(nombre)
        instancia.guardar_datos_csv(instancia, nombre)
        instancia.guardar_datos_csv_bicicleta(instancia, nombre)
        instancia.guardar_datos_csv_globales(instancia, nombre)
        instancia.leer_datos_cvs(nombre)
        lista_bicicletas.append(instancia)
        contador += 1
        
    verificar_instancias(lista_bicicletas)
    



def crear_motocileta():
    lista_motocicletas = []
    opcion = ""
    
    while type(opcion) != int:
    
        try:
            opcion = int(input("Cuantas Motocicletas desea insertar: "))
            
                
        except ValueError:
            print("Ingrese un numero valido")

    contador = 0 
    while contador != opcion:
        numero_ruedas = ""
        tipos = ["Urbana", "Carrera", "1", "2"]
        tipo = ""
        nmro_radios = ""
        
        marca = input("Inserte la Marca de la Motocicleta: ")
        modelo = input("Inserte el Modelo: ")
        while type(numero_ruedas) != int:
            try:
                numero_ruedas = int(input("Inserte el Numero de Ruedas: "))
            except ValueError:
                print("Ingrese un numero valido")
        
        while tipo not in tipos:
            try:
                print("Inserte un tipo de Motocicleta\n1 - Urbana\n2 - Carrera")
                tipo = input("tipo: ").capitalize()
                if tipo == "1":
                    tipo = "Urbana"
                elif tipo == "2":
                    tipo = "Carrera"
        

            except:
                pass
        
        while type(nmro_radios) != int:
            try:
                nmro_radios = int(input("Inserte el Numero de Radios: "))
            except ValueError:
                print("Ingrese un numero valido")
        
        cuadro = input("Inserte el Cuadro: ")
        motor = input("Inserte el Motor: ")

       
        limpiar_pantalla(1)        
        instancia = Motocicleta(marca, modelo, numero_ruedas, tipo, nmro_radios, cuadro, motor)
        limpiar_pantalla(1)
        nombre = random.randint(1, 1000)
        nombre = str(nombre)
        instancia.guardar_datos_csv(instancia, nombre)
        instancia.guardar_datos_csv_motocicleta(instancia, nombre)
        instancia.guardar_datos_csv_globales(instancia, nombre)
        instancia.leer_datos_cvs(nombre)
        lista_motocicletas.append(instancia)
        contador += 1
            
    
        
    verificar_instancias(lista_motocicletas)
   



def leer_datos_csv(nombre_archivo, clase):
    limpiar_pantalla(1)
    vehiculos = []
    salir = False
    while salir != True:
        try:
            archivo = open(nombre_archivo, "r")
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                if len(vehiculo) != 0:
                    vehiculos.append(vehiculo)
            archivo.close()
            salir = True
            print(f"Datos del Archivo: {nombre_archivo}")
            print(f"Lista de Vehiculos {clase}")
            for vehiculo in vehiculos:
                print(vehiculo)
        
        except FileNotFoundError:
            print("El archivo ingresado no se encuentra en el directorio")
            print("Fabrique un vehiculo, en la opcion 1 del menu principal, esto generara un documentos que se podran leer")
            print("Se generara un documento tanto general, es decir de todos los Vehiculos, uno por Clases y uno individual")
            print("Tanto el documento general como los por clases, se alojaran la carpeta principal, y los individuales se alojaran el la carpeta: instancias_creadas")
            salir = True
    



def verificar_instancias(lista):
    print(f"Imprimiendo por pantalla los Vehiculos de clase: {type(lista[0]).__name__}")
    for instancia in lista:
        print(f"Datos de Vehiculo de Clase: {type(instancia).__name__}, numero: {lista.index(instancia) + 1}: {instancia}")
    limpiar_pantalla(6)
    print("Verificando Instancias")
    print(f"Vehiculo de clase {type(instancia).__name__} es instancia con relación a Vehículo: {isinstance(instancia, Vehiculo)}")
    print(f"Vehiculo de clase {type(instancia).__name__} es instancia con relación a Automovil: {isinstance(instancia, Automovil)}")
    print(f"Vehiculo de clase {type(instancia).__name__} es instancia con relación a Vehículo particular: {isinstance(instancia, Particular)}")
    print(f"Vehiculo de clase {type(instancia).__name__} es instancia con relación a Vehículo de carga: {isinstance(instancia, Carga)}")
    print(f"Vehiculo de clase {type(instancia).__name__} es instancia con relación a Bicicleta: {isinstance(instancia, Bicicleta)}")
    print(f"Vehiculo de clase {type(instancia).__name__} es instancia con relación a Motocicleta: {isinstance(instancia, Motocicleta)}")
    limpiar_pantalla(8)


