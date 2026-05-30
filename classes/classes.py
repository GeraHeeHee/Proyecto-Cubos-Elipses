from p5 import *

class Borde:
    def __init__(self, grosor, color):
        self.grosor = grosor
        self.color = color

    def __str__(self):
        return f"grosor={self.grosor}, color={self.color}"

class Dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"width={self.width}, height={self.height}"
    
class Posicion:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __str__(self):
        return f"coord_x={self.coord_x}, coord_y={self.coord_y}"

class Velocidad:
    def __init__(self, vel_x, vel_y):
        self.x = vel_x
        self.y = vel_y

    def __str__(self):
        return f"vel_x={self.x}, vel_y={self.y}"

class Relleno:
    def __init__(self, fill):
        self.fill = fill
    def __str__(self):
        return f"fill={self.fill}"
    
class Figura:

    def __init__(self, borde_grosor, borde_color, width, height, x, y, relleno, vel_x=3, vel_y=3, borde:Borde=None):
        if borde is None:
            self.borde = Borde(borde_grosor, borde_color)
        else:
            self.borde = borde

        self.dimension = Dimension(width, height)
        self.posicion = Posicion(x, y)
        self.velocidad = Velocidad(vel_x, vel_y) 
        self.relleno = Relleno(relleno)
    
    def mover_y_rebotar(self, ancho_ventana:int=100, alto_ventana:int=100):
        # 1. Modificar la posición usando la velocidad
        self.posicion.coord_x += self.velocidad.x
        self.posicion.coord_y += self.velocidad.y

        if (self.posicion.coord_x + self.dimension.width) >= ancho_ventana or self.posicion.coord_x <= 0:
            self.velocidad.x *= -1

        if (self.posicion.coord_y + self.dimension.height) >= alto_ventana or self.posicion.coord_y <= 0:
            self.velocidad.y *= -1

    def dibujar(self):
        stroke_weight(self.borde.grosor)
        stroke(self.borde.color)
        fill(self.relleno.fill)
        rect(self.posicion.coord_x, self.posicion.coord_y, self.dimension.width, self.dimension.height)
    
    def __str__(self):
        return f"{self.borde}, {self.dimension}, {self.posicion}, {self.velocidad}, relleno={self.relleno}"
class Cuadrado(Figura):
    ...
class Elipse(Figura):
    def dibujar(self):
        stroke_weight(self.borde.grosor)
        stroke(self.borde.color)
        fill(self.relleno.fill)
        ellipse(self.posicion.coord_x, self.posicion.coord_y, self.dimension.width, self.dimension.height)

if __name__ == "__main__":
    borde = Borde(3, "#132A42")
    print(borde)
    dimension = Dimension(50, 50)
    print(dimension)
    posicion = Posicion(100, 100)
    print(posicion)
    cuadrado = Cuadrado(3, "#132A42", 50, 50, 100, 100, "#000000", 4, -2)
    print(cuadrado)