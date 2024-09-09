# Función para calcular el área de un rectángulo
def areaR(largo, ancho):
    areaRectangular = largo * ancho
    return areaRectangular

# Función para calcular el área de un triángulo
def areaT(base, altura):
    radioTriangular = 0.5 * base * altura
    return radioTriangular

# Función principal
def main():
    datoLargo = float (input("Ingresa numero lado del rectangulo;"))
    datoAncho = float (input("Ingresa numero  ancho del rectangulo;"))
    rect_area = areaR(datoLargo, datoAncho)
    print("Área del rectángulo:", rect_area)

    datoBase = float (input("Ingresa numero de la base del triangulo;"))
    datoAltura = float (input("Ingresa numero de la altura del triangulo ;"))
    tri_area = areaT(datoBase, datoAltura)
    print("Área del triángulo:", tri_area)

main()
