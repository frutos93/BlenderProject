#!/usr/bin/python
from PIL import Image, ImageDraw, ImageMath
import colorsys

dimensions = (800, 800)       # dimensiones de la imagen
scale = 1.0/(dimensions[0]/3) # lo escalamos
center = (2.2, 1.5)           # Centro de la imagen
iterate_max = 100             # Iteraciones
colors_max = 500              # Numero maximo de colores en la paleta

img = Image.new("RGB", dimensions) # Creamos la imagen
d = ImageDraw.Draw(img)            # Con la varibale d dibujaremoss

# Calculamos los colores de la paleta
palette = [0] * colors_max
for i in xrange(colors_max):
    f = 1 - abs((float(i)/colors_max-1)**15)
    r, g, b = colorsys.hsv_to_rgb(.66+f/3, 1-f/2, f)
    palette[i] = (int(r*255), int(g*255), int(b*255))
palette[colors_max-1] = (0,0,0)

# Verificamos si el punto C pertenece al conjunto de Madelbrot
def iterate_mandelbrot(c):
    z = 0
    for n in xrange(iterate_max + 1):
        z = z*z +c
        if abs(z) > 2: # Si el absoluto de Z > 2 se esta seguro que no pertenece al conjunto
            return n   # Regresamos en que iteracion encontramos el termino que descarto al punto C
    return None

# Dibujamos la imagen
for y in xrange(dimensions[1]):
    for x in xrange(dimensions[0]):
        # Generamos el punto C complejo que vamos a checar
        c = complex(x * scale - center[0], y * scale - center[1])

        # Revisamos si C pertenece al conjunto de Mandelbrot
        n = iterate_mandelbrot(c)

        # Si n fue nulo, C pertenece al conjunto
        if n is None:
            v = 1
        else:
            v = n/100.0 # Si no pertenece al conjunto, elegimos un color de a cuerdo a que tan rapido fue descartado el numero

        # Coloremos el punto
        d.point((x, y), fill = palette[int(v * (colors_max-1))])

del d
img.save("result2.png")
# Codigo original de: http://0pointer.de/blog/projects/mandelbrot.html