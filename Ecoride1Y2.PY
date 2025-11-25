import os
from usuarios import validar_credenciales
from empleados import menu_empleados
from vacaciones import menu_vacaciones
from reportes import generar_reporte

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    print("\n" + "="*50)
    print("   SISTEMA DE GESTIÓN DE VACACIONES - RIWI")
    print("="*50)
    print("1. Gestión de Empleados")
    print("2. Gestión de Vacaciones")
    print("3. Generar Reporte CSV")
    print("4. Salir")
    print("="*50)

def main():
    limpiar_pantalla()
    print("\n" + "="*50)
    print("   INICIO DE SESIÓN - PEOPLE OPERATIONS")
    print("="*50)
    
    usuario = input("\nUsuario: ")
    contrasena = input("Contraseña: ")
    
    if validar_credenciales(usuario, contrasena):
        print("\n✓ Inicio de sesión exitoso")
        input("Presione Enter para continuar...")
        
        while True:
            limpiar_pantalla()
            mostrar_menu_principal()
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                menu_empleados()
            elif opcion == "2":
                menu_vacaciones()
            elif opcion == "3":
                generar_reporte()
            elif opcion == "4":
                print("\n¡Hasta pronto!")
                break
            else:
                print("\n✗ Opción inválida")
                input("Presione Enter para continuar...")
    else:
        print("\n✗ Credenciales incorrectas")

if __name__ == "__main__":
    main()
