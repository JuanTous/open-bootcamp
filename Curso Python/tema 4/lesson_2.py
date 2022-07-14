if __name__ == "__main__":
    numero_inicial: int = int(input('Introduce un número: '))
    numero_final: int = int(input('Inroduce otro número: '))
    numeros_impares: [int] = []

    for i in range(numero_inicial, numero_final+1):
        if(i % 2 != 0):
            numeros_impares.append(i)

    print(f"Lista de Números impares entre {numero_inicial} y {numero_final} es:")
    print(numeros_impares)