if __name__ == "__main__":
    peso = input("Ingresa tu peso en kg: ")
    estatura = input("Ingresa tu estatura en metros: ")
    imc = round(float(peso)/float(estatura)**2,2)
    
    print("Su índice de masa corporal es " + str(imc))