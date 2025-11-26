import csv
import os

def validar_credenciales(usuario, contrasena):
    """Valida las credenciales contra el archivo usuarios.csv"""
    if not os.path.exists('usuarios.csv'):
        # Crear archivo con usuario admin por defecto
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['usuario', 'contrasena', 'rol'])
            writer.writerow(['admin', 'admin123', 'administrador'])
    
    with open('usuarios.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['usuario'] == usuario and row['contrasena'] == contrasena:
                return True
    return False
