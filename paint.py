"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Dibuja un círculo relleno utilizando dos puntos seleccionados
    por el usuario.

    Parámetros:
        start (vector): Punto inicial donde comienza el círculo.
        end (vector): Punto utilizado para calcular el radio."""
    # Levanta la pluma para moverse sin dibujar.
    up()
    # Se coloca en el punto inicial.
    goto(start.x, start.y)
    # Baja la pluma para comenzar a dibujar.
    down()
    # Calcular el radio tomando la distancia horizontal entre el punto inicial y final.

    radius = abs(end.x - start.x)

    # Comienza a rellenar la figura.
    begin_fill()
    dot(radius * 2)
    # Termina el relleno del círculo.
    end_fill()


def rectangle(start, end):
    """Draw a rectangle from start to end.

    Args:
        start: Initial point of the rectangle.
        end: Opposite point of the rectangle.

    Returns:
        None.
    """

    # Levanta la pluma para moverse sin dibujar.
    up()

    # Coloca la tortuga en el punto inicial.
    goto(start.x, start.y)

    # Baja la pluma para comenzar a dibujar.
    down()

    # Comienza a rellenar la figura.
    begin_fill()

    # Repite el proceso dos veces para dibujar
    # los cuatro lados del rectangulo.
    for count in range(2):

        # Dibuja el lado horizontal.
        forward(end.x - start.x)

        # Gira 90 grados hacia la izquierda.
        left(90)

        # Dibuja el lado vertical.
        forward(end.y - start.y)

        # Gira 90 grados para continuar
        # con el siguiente lado.
        left(90)

    # Termina el relleno del rectangulo.
    end_fill()


def triangle(start, end):
    """Draw an equilateral triangle from start to end.

    Args:
        start: Initial point of the triangle.
        end: Point used to determine the side length.

    Returns:
        None.
    """

    # Levanta la pluma para moverse sin dibujar.
    up()

    # Coloca la tortuga en el punto inicial.
    goto(start.x, start.y)

    # Baja la pluma para comenzar a dibujar.
    down()

    # Comienza a rellenar la figura.
    begin_fill()

    # Repite el proceso tres veces,
    # una por cada lado del triangulo.
    for count in range(3):

        # Dibuja un lado del triangulo.
        forward(end.x - start.x)

        # Gira 120 grados para formar
        # un triangulo equilatero.
        left(120)

    # Termina el relleno del triangulo.
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
# Nuevo color agregado 
# Al presionar la tecla P se selecciona el color morado.
onkey(lambda: color('purple'), 'P')      
done()
