
# Importa randrange para generar posiciones aleatorias.
# AGREGADO: sample para elegir colores aleatorios sin repetir.
from random import randrange, sample

from turtle import *
from freegames import square, vector

# Posición inicial de la comida.
food = vector(0, 0)

# Posición inicial de la víbora.
snake = [vector(10, 0)]

# Dirección inicial de movimiento.
aim = vector(0, -10)

# AGREGADO: lista de los 5 colores permitidos.
# Se excluye el rojo para los colores de la víbora y la comida.
colors = ['black', 'blue', 'green', 'yellow', 'purple']

# AGREGADO: selecciona dos colores diferentes al azar.
# El primer color corresponde a la víbora y el segundo a la comida.
snake_color, food_color = sample(colors, 2)


# Cambia la dirección de movimiento de la víbora.
def change(x, y):
    aim.x = x
    aim.y = y


# Comprueba que la cabeza permanezca dentro de la ventana.
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


# Controla el movimiento y funcionamiento del juego.
def move():
    # Calcula la nueva posición de la cabeza.
    head = snake[-1].copy()
    head.move(aim)

    # Comprueba si la víbora salió de la ventana o chocó consigo misma.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # Agrega la nueva posición de la cabeza.
    snake.append(head)

    # Comprueba si la víbora comió.
    if head == food:
        print('Snake:', len(snake))

        # Genera una nueva posición aleatoria para la comida.
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # Elimina el último segmento para mantener el tamaño.
        snake.pop(0)

    # Limpia la pantalla antes de dibujar el nuevo estado.
    clear()

    # AGREGADO: dibuja la víbora con su color aleatorio.
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # AGREGADO: dibuja la comida con un color diferente.
    square(food.x, food.y, 9, food_color)

    # Actualiza la pantalla.
    update()

    # Programa el siguiente movimiento.
    ontimer(move, 100)


# Configuración de la ventana del juego.
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Controles para cambiar la dirección de la víbora.
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Inicia el juego.
move()
done()
