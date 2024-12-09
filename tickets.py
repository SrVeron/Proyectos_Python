import pickle, sys, os, random

ARCHIVO_TURNOS = "ticket.pkl"

def limpiar_pantalla():
    os.system("clear" if os.name == "posix" else "cls")

def numero_ticket():
    return random.randint(1000,9999)

def guardar_ticket(tickets):
    with open(ARCHIVO_TURNOS, "wb") as f:
        pickle.dump(tickets,f)
    
def cargar_tickets():
    if os.path.isfile(ARCHIVO_TURNOS):
        with open(ARCHIVO_TURNOS,"rb") as f:
            return pickle.load(f)
    else:
        return{}

tickets = cargar_tickets()

def generar_ticket():
    nombre = input("Ingrese su nombre: ")
    especialidad = input("Seleccione una especialidad: ")
    obra = input("Ingrese su obra social: ")
    
    numero_orden = numero_ticket()
    
    tickets[numero_orden]={
        "Nombre": nombre,
        "Especialida": especialidad,
        "Obra Social": obra
    }
    
    guardar_ticket(tickets)

    print(f"Entrada generada con éxito. Su número de orden es: {numero_orden}")
    print("Aguarde y será atendido por su número de orden")
    
    input("Presione Enter para continuar")
    
    
def leer_ticket():
    numero_orden = int(input("Ingrese el número de orden: "))
    
    if numero_orden in tickets:
        ticket = tickets[numero_orden]
        print("Información de la orden: ")
        for key, value in ticket.items():
            print(f"{key}: {value}")
        print()
    else:
        print("El número de orden ingresado no existe.")
        
    input("Presione Enter para continuar")

def menu():
    while True:
        limpiar_pantalla()
        print("Bienvenido al sistema de Turnos")
        print("1 - Generar nueva orden")
        print("2 - Leer orden")
        print("3 - Salir")
        opcion = input("Seleccione: ")
        
        if opcion == "1":
            generar_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            confirmacion = input("¿Está seguro de que desea salir? (s/n): ")
            if confirmacion.lower() == "s":
                print("Gracias por usar nuestro sistema de Turnos")
                sys.exit()
        else:
            print("Opción no válida, intente de nuevo")
            
menu()