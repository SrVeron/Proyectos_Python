import pickle, sys, os, random

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

numero_random = random.randrange(1000,9999)
print(f"Número de ticket: {numero_random}")

ticket = {"numero": numero_random}
nombre_archivo = "ticket.pkl"

with open(nombre_archivo, "wb") as f:
    pickle.dump(ticket,f)
print(f"Ticket guardado en el archivo: {nombre_archivo}")

if os.path.isfile(nombre_archivo):
    with open(nombre_archivo, "rb") as f:
        ticket_cargado = pickle.load(f)
    print(f"Ticket cargado: {ticket_cargado}")
else:
    print(f"El archivo {nombre_archivo} no existe")

sys.exit()