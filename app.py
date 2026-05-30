from p5 import *
from classes.classes import *
from patron.Builders import *
import random  

ancho_ventana = 600
alto_ventana = 600
figuras = []

def setup():
    global ancho_ventana, alto_ventana, figuras
    size(ancho_ventana, alto_ventana)

    cantidad_figuras = random.randint(10, 25)

    for _ in range(cantidad_figuras):
        tipo_aleatorio = random.randint(0, 1)
        
        nueva_figura = crearFiguraAleatoria(tipo_aleatorio)
        figuras.append(nueva_figura)

def draw():
    background(240) 

    for figura in figuras:
        interacturarObj(figura)

def interacturarObj(figura: Figura):
    figura.dibujar()
    figura.mover_y_rebotar(ancho_ventana, alto_ventana)

def generar_color_hex_aleatorio():
    """Genera un color en formato hexadecimal '#RRGGBB' de forma aleatoria."""
    letras = "0123456789ABCDEF"
    color = "#" + "".join(random.choice(letras) for _ in range(6))
    return color

def crearFiguraAleatoria(tipo: int):
    
    tamano = random.randint(30, 80)
    
    pos_x = random.randint(0, ancho_ventana - tamano)
    pos_y = random.randint(0, alto_ventana - tamano)
    
    vel_x = random.choice([-5, -4, -3, 3, 4, 5])
    vel_y = random.choice([-5, -4, -3, 3, 4, 5])
    
    color_relleno = generar_color_hex_aleatorio()
    color_borde = generar_color_hex_aleatorio()
    grosor_borde = random.randint(1, 4)

    builder = (Builder()
               .configBorde(grosor_borde, color_borde)
               .configColor(color_relleno)
               .configDimension(tamano, tamano)
               .configPosiciones(pos_x, pos_y)
               .configVelocidad(vel_x, vel_y))
    
    if tipo == 1:
        builder.esElipse()
        
    return builder.build()

if __name__ == "__main__":
    run()