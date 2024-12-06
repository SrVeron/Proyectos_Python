from random import randrange

def pantalla_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)
    print()


def movimiento_usuario(tablero):
    while True:
        try:
            fila = int(input("¿En qué fila? 0, 1 o 2"))
            col = int(input("¿En qué columna? 0, 1 o 2"))
            if tablero[fila][col] == " ":
                tablero[fila][col] = "X"
                break
            else:
                print("Ese espacio ya está ocupado :(")
        except(IndexError, ValueError):
            print("Por favor, ingrese números válidos para filas o columnas")
            
def movimiento_maquina(tablero):
    while True:
        fila = randrange(3)
        col = randrange(3)
        if tablero [fila][col] == " ":
            tablero [fila][col] = "O"
            break
        
def victoria(tablero, jugador):
    for fila in tablero:
        if all(espacio == jugador for espacio in fila):
            return True
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def empate(tablero):
    return all(tablero[fila][col] != " " for fila in range(3) for col in range(3))
    
        
def main():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno = "usuario" if randrange(2) == 0 else "maquina"
    
    while True:
        pantalla_tablero(tablero)
        if turno == "usuario":
            movimiento_usuario(tablero)
            if victoria(tablero, "X"):
                pantalla_tablero(tablero)
                print("Ganaste! Felicidades!")
                break
            turno = "maquina"
        else:
            movimiento_maquina(tablero)
            if victoria(tablero,"O"):
                pantalla_tablero(tablero)
                print("Perdiste, intentá de nuevo")
                break
            turno = "usuario"
            if empate(tablero):
                pantalla_tablero(tablero)
                print("Empataron, intentá de nuevo")
                break
if __name__ == "__main__":
    main()