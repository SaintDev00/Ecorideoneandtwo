import csv
import os

def inicializar_archivo_empleados():
    """Crea el archivo empleados.csv si no existe"""
    if not os.path.exists('empleados.csv'):
        with open('empleados.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['empleado_id', 'nombre_completo', 'cargo', 'area', 'fecha_inicio_contrato'])

def registrar_empleado():
    """Registra un nuevo empleado"""
    inicializar_archivo_empleados()
    
    print("\n--- REGISTRAR EMPLEADO ---")
    empleado_id = input("ID del empleado: ")
    nombre = input("Nombre completo: ")
    cargo = input("Cargo: ")
    area = input("Área: ")
    fecha_inicio = input("Fecha de inicio (DD/MM/AAAA): ")
    
    with open('empleados.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([empleado_id, nombre, cargo, area, fecha_inicio])
    
    print(f"\n✓ Empleado {nombre} registrado exitosamente")
    input("Presione Enter para continuar...")

def listar_empleados():
    """Muestra todos los empleados registrados"""
    inicializar_archivo_empleados()
    
    print("\n--- LISTA DE EMPLEADOS ---")
    with open('empleados.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        empleados = list(reader)
        
        if not empleados:
            print("No hay empleados registrados")
        else:
            for emp in empleados:
                print(f"\nID: {emp['empleado_id']}")
                print(f"Nombre: {emp['nombre_completo']}")
                print(f"Cargo: {emp['cargo']}")
                print(f"Área: {emp['area']}")
                print("-" * 40)
    
    input("\nPresione Enter para continuar...")

def consultar_empleado():
    """Muestra información detallada de un empleado"""
    inicializar_archivo_empleados()
    
    print("\n--- CONSULTAR EMPLEADO ---")
    empleado_id = input("Ingrese ID del empleado: ")
    
    with open('empleados.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        encontrado = False
        
        for emp in reader:
            if emp['empleado_id'] == empleado_id:
                print(f"\n{'='*40}")
                print(f"ID: {emp['empleado_id']}")
                print(f"Nombre: {emp['nombre_completo']}")
                print(f"Cargo: {emp['cargo']}")
                print(f"Área: {emp['area']}")
                print(f"Fecha de inicio: {emp['fecha_inicio_contrato']}")
                print(f"{'='*40}")
                encontrado = True
                break
        
        if not encontrado:
            print(f"\n✗ Empleado con ID {empleado_id} no encontrado")
    
    input("\nPresione Enter para continuar...")

def menu_empleados():
    """Menú de gestión de empleados"""
    while True:
        print("\n" + "="*50)
        print("   GESTIÓN DE EMPLEADOS")
        print("="*50)
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Consultar empleado")
        print("4. Volver al menú principal")
        print("="*50)
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            consultar_empleado()
        elif opcion == "4":
            break
        else:
            print("\n✗ Opción inválida")
            input("Presione Enter para continuar..."
