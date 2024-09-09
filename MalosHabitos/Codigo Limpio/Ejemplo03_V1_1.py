# Función para calcular el área de un rectángulo
def AreaRectangular(largo, ancho):
    areaRectangular = largo * ancho
    return areaRectangular


# Función para calcular el área de un triángulo
def AreaTriangular(base, altura):
    radioTriangular = 0.5 * base * altura
    return radioTriangular


# Función principal
def main():
    datoLargo = float(input("Ingresa número lado del rectangulo:"))
    datoAncho = float(input("Ingresa número  ancho del rectangulo:"))
    rect_area = AreaRectangular(datoLargo, datoAncho)
    print("Área del rectángulo:", rect_area)

    datoBase = float(input("Ingresa numero de la base del triangulo:"))
    datoAltura = float(input("Ingresa numero de la altura del triangulo:"))
    tri_area = AreaTriangular(datoBase, datoAltura)
    print("Área del triángulo:", tri_area)


main()
