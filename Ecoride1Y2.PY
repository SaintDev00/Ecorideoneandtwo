#EcoRide Alquiler de Bicicletas Sostenibles

#Mostrar mensaje de bienvenida. 
print("=" * 60)
print("BIENVENIDO A ECORIDE MOVILIDAD SOSTENIBLE")
print("=" * 60)
print()

# Variables de tarifas (FLOAT)
tarifa_premium = 0.85
tarifa_estandar = 0.50
penalizacion = 5.00
descuento = 0.10
recargo_finde = 0.05

#Bucle principal
while True:
    print("\n" + "=" * 60)
    print("MENÚ PRINCIPAL")
    print("=" * 60)
    print("1. Alquilar Bicicleta")
    print("2. Consultar Tarifas")
    print("3. Información Descuentos")
    print("4. Salir Del Sistema")
    print("=" * 60)
    
    opcion_menu = int(input("Seleccione una opción (1-4): "))
    
    if opcion_menu == 1:    
        #Proceso Alquiler Bicicleta
        print("\n" + "-" * 60)  
        print("ESCOJA EL TIPO DE BICICLETA")
        print("-" * 60)
        print("1. Premium - €{:.2f}/min".format(tarifa_premium))
        print("2. Estándar - €{:.2f}/min".format(tarifa_estandar))
        
        opcion_bicicleta = int(input("Seleccione (1-2): "))
        
        #Variables STRING y FLOAT
        nombre_bici = ""
        tarifa = 0.0
        
        #Condicional para tipo de bici
        if opcion_bicicleta == 1:
            nombre_bici = "Premium"
            tarifa = tarifa_premium
            print("✓ Bicicleta Premium seleccionada")
        elif opcion_bicicleta == 2:
            nombre_bici = "Estándar"
            tarifa = tarifa_estandar
            print("✓ Bicicleta Estándar seleccionada")
        else:
            print("✗ Opción inválida")
            continue
        
        #Solicitar tiempo de uso (ENTERO)
        tiempo = 0
        while tiempo <= 0:
            tiempo = int(input("\nIngrese minutos de uso: "))
            if tiempo <= 0:
                print("✗ El tiempo debe ser mayor a 0")
        
        print("✓ Tiempo registrado: {} minutos".format(tiempo))
        
        #Calcular costo base (FLOAT)
        costo_base = tiempo * tarifa
        
        #Preguntar si es fin de semana (STRING)
        while True:
            finde = input("\n¿Es fin de semana? (si/no): ").lower()
            if finde == "si" or finde == "no":
                break
            print("✗ Error: Responda 'si' o 'no'")
        
        #Preguntar devolución a tiempo (STRING)
        while True:
            devolucion = input("¿Devolverá a tiempo? (si/no): ").lower()
            if devolucion == "si" or devolucion == "no":
                break
            print("✗ Error: Responda 'si' o 'no'")
        
        #Método de pago (STRING)
        print("\n" + "-" * 60)
        print("MÉTODO DE PAGO")
        print("-" * 60)
        print("1. Efectivo")
        print("2. Tarjeta")
        print("3. Puntos")
        
        metodo_pago = int(input("Seleccione (1-3): "))
        
        nombre_pago = ""
        if metodo_pago == 1:
            nombre_pago = "Efectivo"
        elif metodo_pago == 2:
            nombre_pago = "Tarjeta"
        elif metodo_pago == 3:
            nombre_pago = "Puntos"
        else:
            nombre_pago = "Efectivo"
            metodo_pago = 1
        
        #Variables para descuentos y recargos (FLOAT)
        desc = 0.0
        rec = 0.0
        penal = 0.0
        
        print("\n" + "-" * 60)
        print("PROCESANDO...")
        print("-" * 60)
        
        #Condicional Anidada .Descuento
        if tiempo > 60:
            if metodo_pago == 2:
                desc = costo_base * descuento
                print("✓ Descuento aplicado: >60 min + tarjeta (-10%)")
        else:
            if tiempo < 10 and metodo_pago == 3:
                print("• Sin descuento: <10 min + puntos")
        
        #Recargo fin de semana
        if finde == "si":
            rec = costo_base * recargo_finde
            print("✓ Recargo fin de semana aplicado (+5%)")
        
        #Penalización por retraso
        if devolucion == "no":
            penal = penalizacion
            print("✓ Penalización por retraso (+€{:.2f})".format(penal))
        
        #Calcular total(FLOAT)
        total = costo_base - desc + rec + penal
        
        #Mostrar resumen
        print("\n" + "=" * 60)
        print("RESUMEN DEL SERVICIO")
        print("=" * 60)
        print("Tipo de bicicleta:    {}".format(nombre_bici))
        print("Tiempo de uso:        {} minutos".format(tiempo))
        print("Método de pago:       {}".format(nombre_pago))
        print("-" * 60)
        print("Costo base:           €{:.2f}".format(costo_base))
        
        if desc > 0:
            print("Descuento:            -€{:.2f}".format(desc))
        if rec > 0:
            print("Recargo:              +€{:.2f}".format(rec))
        if penal > 0:
            print("Penalización:         +€{:.2f}".format(penal))
        
        print("-" * 60)
        print("TOTAL A PAGAR:        €{:.2f}".format(total))
        print("=" * 60)
        
        #Preguntar si desea continuar (BOOLEANO)
        continuar_resp = input("\n¿Desea realizar otro alquiler? (si/no): ").lower()
        if continuar_resp != "si":
            print("\n¡Gracias por usar EcoRide!")
            break
    
    elif opcion_menu == 2:
        #Consultar Tarifas
        print("\n" + "=" * 60)
        print("TARIFAS ECORIDE")
        print("=" * 60)
        print("Bicicleta Estándar:   €{:.2f}/min".format(tarifa_estandar))
        print("Bicicleta Premium:    €{:.2f}/min".format(tarifa_premium))
        print("Penalización retraso: €{:.2f}".format(penalizacion))
        print("=" * 60)
        input("\nPresione Enter para volver al menú...")
    
    elif opcion_menu == 3:
        #Información Descuentos
        print("\n" + "=" * 60)
        print("DESCUENTOS Y RECARGOS")
        print("=" * 60)
        print("DESCUENTOS:")
        print("• Uso >60 min + tarjeta: -10%")
        print("\nRECARGOS:")
        print("• Fin de semana: +5%")
        print("• Devolución tardía: +€{:.2f}".format(penalizacion))
        print("\nNOTA:")
        print("• Uso <10 min + puntos: sin descuento")
        print("=" * 60)
        input("\nPresione Enter para volver al menú...")
    
    elif opcion_menu == 4:
        #Salir
        print("\n¡Gracias por usar EcoRide!")
        print("Movilidad sostenible para un mejor futuro")
        break
    
    else:
        print("\n✗ Opción inválida. Seleccione 1-4")