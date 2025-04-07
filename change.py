def change():
    expense = 23.75
    money = 100

    print("Igresar gasto: ")
    print(expense)
    print("Dinero recibido: ")
    print(money)

    vuelto = money - expense

    pesos = int(vuelto)
    centavos = int((vuelto-pesos)*100)
    print("vuelto")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
