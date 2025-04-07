def change():
    expense = 23.75
    money = 100
    
    vuelto = money - expense

    pesos = int(vuelto)
    centavos = int((vuelto-pesos)*100)
    print("small_chage")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
