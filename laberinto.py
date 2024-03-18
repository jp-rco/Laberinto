from time import sleep

def solucion(formato, filas, col):
    lab = []
    for i in range(filas):
        fila = []
        for j in range(col):
            fila.append(formato[i*col + j])
        lab.append(fila)

    def movimiento(x, y):
        if x < 0 or y < 0 or x >= filas or y >= col:
            return False
        if lab[x][y] == '+' or lab[x][y] == 'o':
            return False
        return True

    def imprimir_lab():
        print('+' + '-' * (col * 4 - 1) + '+')
        for fila in lab:
            print('| ' + '   '.join(fila) + ' |')
        print('+' + '-' * (col * 4 - 1) + '+')

    def salida(x, y, movimientos):
        if not movimiento(x, y):
            return False
        if lab[x][y] == 'X':

            lab[x][y] = '@'
            imprimir_lab()
            print("Movimientos: ", movimientos)
            print()
            sleep(tiempo / 1000)
            print("¡Hemos encontrado una solción!. Aquí te dejamos el paso final." )
            return True
        lab[x][y] = '@'
        imprimir_lab()
        print("Movimientos: ", movimientos)
        print()
        sleep(tiempo / 1000)
        lab[x][y] = 'o'
        if (
                salida(x + 1, y, movimientos + 1)
                or salida(x - 1, y, movimientos + 1)
                or salida(x, y + 1, movimientos + 1)
                or salida(x, y - 1, movimientos + 1)
        ):
            return True
        lab[x][y] = ' '
        return False

    inicio_x, inicio_y = None, None
    for i in range(filas):
        for j in range(col):
            if lab[i][j] == 'O':
                inicio_x, inicio_y = i, j
                break

    if salida(inicio_x, inicio_y, 0):
        lab[inicio_x][inicio_y] = 'O'
        imprimir_lab()
    else:
        print("No hemos podido encontrar una solución ;")


filas = int(input("Ingresa el tamaño del laberinto: "))
formato = input("Ingresa el formato del laberinto: ")
tiempo = float(input("Ingresa el tiempo en milisegundos de espera para el movimiento de la limbríz dentro del laberinto: "))
col = filas
solucion(formato,filas, col)