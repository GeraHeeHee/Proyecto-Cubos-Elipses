from classes.classes import *

class Builder:
    
    def __init__(self):
        self._borde_grosor = 1
        self._borde_color = "#000000"
        self._color_relleno = "#FFFFFF"
        self._width = 50
        self._height = 50
        self._x = 0
        self._y = 0
        self._vel_x = 3
        self._vel_y = 3
        self._esElipse = False 

    def configBorde(self, borde_grosor, borde_color):
        self._borde_color = borde_color
        self._borde_grosor = borde_grosor
        return self 
    
    def configColor(self, color:str):
        self._color_relleno = color
        return self
    
    def configPosiciones(self, x:float, y:float):
        self._x = x
        self._y = y
        return self

    def configDimension(self, width: int = 50, height: int = 50):
        self._width = width
        self._height = height
        return self
    
    def configVelocidad(self, vel_x:float, vel_y:float):
        self._vel_x = vel_x
        self._vel_y = vel_y
        return self
    
    def esElipse(self):
        self._esElipse = True
        return self
    
    def build(self):
        variable = {
            'width': self._width, 
            'height': self._height,
            'borde_grosor': self._borde_grosor,
            'borde_color': self._borde_color,
            'x': self._x,
            'y': self._y,
            'color_relleno': self._color_relleno,
            'vel_x': self._vel_x,
            'vel_y': self._vel_y
        }
        
        if not self._esElipse:
            return Cuadrado(borde_grosor = variable['borde_grosor'], borde_color = variable['borde_color'], 
                            height=variable['height'], width=variable['width'], 
                            x=variable['x'], y=variable['y'], 
                            relleno = variable['color_relleno'], 
                            vel_x=variable['vel_x'], vel_y=variable['vel_y'])  
        else:
            return Elipse(borde_grosor = variable['borde_grosor'], borde_color = variable['borde_color'], 
                          height=variable['height'], width=variable['width'], 
                          x=variable['x'], y=variable['y'], 
                          relleno = variable['color_relleno'], 
                          vel_x=variable['vel_x'], vel_y=variable['vel_y'])