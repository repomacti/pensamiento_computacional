import matplotlib.pyplot as plt
import macti.visual as mvis

def grafica(x, y1, y2, sol = [], xs = [], ys = [], vA = [], xg = [], yg = [], z = []):
    """
    Esta función grafica las líneas rectas, los contornos de la 
    función cuadrática, la solución, los pasos y los eigenvectores.

    Parameters
    ----------
    x: ndarray
    Arreglo con las coordenadas en x

    y1: ndarray
    Arreglo con las coordenadas en y para la recta 1.

    y2: ndarray
    Arreglo con las coordenadas en y para la recta 2.

    sol: array (opcional)
    Arreglo con la solución del sistema de 2x2

    xs: array (opcional)
    Arreglo con las coordenadas x de cada iteración, sirve para 
    graficar los pasos que realiza el método.

    ys: array (opcional)
    Arreglo con las coordenadas y de cada iteración, usado para 
    graficar los pasos que realiza el método.

    vA: array (opcional)
    Arreglo de dos vectores que representan los eigenvectores del
    sistema. Usado para graficar los eigenvectores.

    xg: ndarray (opcional)
    Arreglo con las coordenadas x de la rejilla para la graficación
    de los contornos.

    yg: ndarray (opcional)
    Arreglo con las coordenadas y de la rejilla para la graficación
    de los contornos.

    z: ndarray (opcional)
    Arreglo con los valores de la función cuadrática para la graficación
    de los contornos. 

    NOTA: Se deben dar xg, yg y z para que los contornos se puedan graficar.

    
    """
    
    # Graficamos las líneas rectas
    plt.plot(x, y1, lw = 3, c = 'seagreen', label = '$3x+2y=2$') # Línea recta 1
    plt.plot(x, y2, lw = 3, c = 'mediumorchid', label = '$2x+6y=-8$') # Línea recta 2

    if len(sol):
        # Graficamos la solución
        plt.scatter(sol[0], sol[1], fc='sandybrown', ec='k', s = 75, alpha=0.75, zorder=5, label='Solución final         .') # Solución

    if len(xs) and len(ys):
        # Graficamos los pasos
        plt.scatter(xs[0], ys[0], fc='yellow', ec='k', s = 75, alpha=0.75, zorder=8, label='Solución inicial')
        plt.scatter(xs[1:], ys[1:], c='navy', s = 10, alpha=0.5, zorder=8)
        plt.plot(xs, ys, c='grey', ls = '--', lw=1.0, zorder=8, label='Pasos del método')

    if len(vA):
        # Graficamos los eigenvectores
        plt.quiver([sol[0], sol[0]], [sol[1], sol[1]], vA[0], vA[1], scale=10, zorder=9)

    if len(xg) and len(yg) and len(z):
        plt.contour(xg, yg, z, levels = 25, cmap='twilight', linewidths=1.0, zorder=1)        
        
    plt.legend(ncol = 1, frameon=True, loc='best')#, bbox_to_anchor=(1.90, 1.02))
    plt.grid()
    plt.show()