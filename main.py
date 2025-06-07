print("¡Bienvenidos a SkyRoute S.R.L. - Sistema de Gestión de Pasajes para el administrativo pulenta!")
#ciclo"WHILE"
while True:
    print("¡Menú Principal...a por ellos campeón!:")
    print("1. ¿ya miráste los clientes?")
    print("2. Fijáte los destinos, ¡no metás la pata!")
    print("3. ¿Te gusta la platita?, ¡pegale un ojo a las ventas!")
    print("4. ¡Mirá los destinos que elegieron tus viajeros!")
    print("5. ¡No llores!...Botón de Arrepentimiento")
    print("6. Apreta este y te vas al after office")

    opcion = input("¿Alguna opción en especial?, seleccionate una y comenzamos!: ")
    
    #"CONDICIONALES IF-ELSE"
    if opcion == "1":
        print("GESTIONAR CLIENTES")
        print("a. Ver Clientes")
        print("b. Agregar Cliente")
        print("c. Modificar Cliente")
        print("d. Eliminar Cliente")
        print("e. Volver al Menú Principal")
        sub_opcion = str(input("Elegí una opción(¡solo letra, ojito!): "))
        clientes = ["Cliente1", "Cliente2", "Cliente3"] 
        #ciclo"FOR" 
        if sub_opcion == "a":  
            print("Lista de clientes:")
            for cliente in clientes:
                print(f"Tu cliente es: {cliente}") 
        elif sub_opcion == "b":  
            print("agregando clientes:")
            for cliente in clientes:
                print(f"agregaste a: {cliente}") 
        elif sub_opcion == "c":
            print("modificando clientes:")
            for cliente in clientes:
                print(f"modificaste a: {cliente}")  
        elif sub_opcion == "d":
            print("eliminando clientes:")
            for cliente in clientes:
                print(f"eliminaste a: {cliente}")
        elif sub_opcion == "e":
            print("Volviendo al Menú Principal...")
            
        else:
            print("No tenés una goma de clientes registrados. Media pila!")  
        
        
    elif opcion == "2":
        print("1. Ver destinos")
        print("2. Agregar destino")
        print("3. Modificar destino")
        print("4. Eliminar destino")
        print("5. Volver al Menú Principal")
        sub_opcion = int(input("Elegí una opción: "))
        
    elif opcion == "3":
        print("1. Ver ventas")
        print("2. Agregar venta")
        print("3. Modificar venta")
        print("4. Eliminar venta")
        print("5. Volver al Menú Principal")
        sub_opcion = int(input("Elegí una opción: "))
        
    elif opcion == "4":
        print("1. Tangamandapio")
        print("2. Villa Cariño")
        print("3. Fumarola de la Rivera")
        print("4. Loma del Chifle")
        print("5. Volver al Menú Principal")
        sub_opcion = int(input("Elegí una opción: "))
        
    elif opcion == "5":
        print("¡Arrepentite pecador, con el botón de arrepentimiento...!")
        
    elif opcion == "6":
        print("Saliste del sistema, tomate un cervecita!")
        
        break
    
    else:
        print("Opción inválida.¡Escribiste cualquiera!")
