def calcular(variable1, variable2, variable3):
    resuntado  = variable1 * variable2 + variable3
    return resuntado

if __name__=="__main__":
    numero1 = float (input("Ingresa numero 1;"))
    numero2 = float (input("Ingresa numero 2;"))
    numero3 = float (input("Ingresa numero 3;"))
    resultado = calcular(numero1, numero2, numero3)
    print("El resultado es:", resultado)

principal()
