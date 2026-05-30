from p5 import *
from classes.classes import *
from patron.Builders import *

elipse = None
cuadrado2 = None
cuadrado3 = None
elipse2 = None
ancho_ventana = 600
alto_ventana = 600
figuras = []

def setup():
    global elipse
    global elipse2
    global cuadrado2
    global cuadrado3
    global ancho_ventana
    global alto_ventana
    size(ancho_ventana, alto_ventana)

    figuras.append(crearFigura(0))
    figuras.append(crearFigura(1))

def draw():
    background(240) 

    for figura in figuras:
        interacturarObj(figura)

def interacturarObj(figura:Figura):
    figura.dibujar()
    figura.mover_y_rebotar(ancho_ventana, alto_ventana)

def crearFigura(tipo:int):
    if tipo == 0:
        return Builder().configBorde(2,"#000000").configColor("#123400").configDimension(50,50).configPosiciones(0,0).configVelocidad(3,2).build()
    else:
        return Builder().configBorde(2,"#FF0000").configColor("#796EDD").configDimension(50,50).configPosiciones(100,100).configVelocidad(-2,3).esElipse().build()

run()