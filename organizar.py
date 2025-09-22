import os
import shutil

# --- ENTORNO DE PRUEBAS EN CODESPACES ---
downloads_path = '/data/data/com.termux/files/home/storage/shared/Download'

# --- ESTRUCTURA DE CARPETAS ---
# Definimos las carpetas principales. Las subcarpetas se crearán dinámicamente.
carpetas_principales = {
    'Camara Xiaomi': [],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Documentos': ['.pdf', '.docx', '.txt'],
    'Comprimidos': ['.zip', '.rar'],
    'Apps': ['.apk'],
    'Otros': []
}

# --- LÓGICA DEL SCRIPT MEJORADA ---

# Asegurarse de que la carpeta de prueba exista
if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)
    print(f"Carpeta de prueba creada en: '{downloads_path}'")

# Crear todas las carpetas principales si no existen
print("Creando estructura de carpetas principal...")
for carpeta in carpetas_principales.keys():
    ruta_carpeta = os.path.join(downloads_path, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# --- NUEVA SECCIÓN: Crear las subcarpetas dentro de 'Camara Xiaomi' ---
ruta_camara_xiaomi = os.path.join(downloads_path, 'Camara Xiaomi')
subcarpetas_camara = ['Fotos', 'Videos']
for subcarpeta in subcarpetas_camara:
    ruta_subcarpeta = os.path.join(ruta_camara_xiaomi, subcarpeta)
    if not os.path.exists(ruta_subcarpeta):
        os.makedirs(ruta_subcarpeta)
        print(f" -> Subcarpeta '{subcarpeta}' creada en 'Camara Xiaomi'")

print("\nIniciando organización de archivos avanzada...")

# Revisar cada archivo en la carpeta de Descargas de prueba.
for nombre_archivo in os.listdir(downloads_path):
    ruta_archivo_origen = os.path.join(downloads_path, nombre_archivo)

    if os.path.isfile(ruta_archivo_origen):
        
        # --- LÓGICA ANIDADA PARA LA CÁMARA ---
        # 1. ¿Es una foto de la cámara?
        if nombre_archivo.startswith('IMG_'):
            ruta_destino = os.path.join(ruta_camara_xiaomi, 'Fotos')
            shutil.move(ruta_archivo_origen, ruta_destino)
            print(f"📸 Moviendo foto de cámara '{nombre_archivo}' a 'Camara Xiaomi/Fotos'")
            continue # Pasa al siguiente archivo

        # 2. ¿Es un video de la cámara?
        if nombre_archivo.startswith('VID_'):
            ruta_destino = os.path.join(ruta_camara_xiaomi, 'Videos')
            shutil.move(ruta_archivo_origen, ruta_destino)
            print(f"📹 Moviendo video de cámara '{nombre_archivo}' a 'Camara Xiaomi/Videos'")
            continue # Pasa al siguiente archivo

        # --- LÓGICA PARA EL RESTO DE ARCHIVOS (si no era de la cámara) ---
        extension = os.path.splitext(nombre_archivo)[1].lower()
        movido = False
        for carpeta_destino, extensiones_validas in carpetas_principales.items():
            if carpeta_destino == 'Camara Xiaomi': # Evitar que algo más vaya a la raíz de esta carpeta
                continue
            
            if extension in extensiones_validas:
                ruta_carpeta_destino = os.path.join(downloads_path, carpeta_destino)
                shutil.move(ruta_archivo_origen, ruta_carpeta_destino)
                print(f" -> Moviendo '{nombre_archivo}' a '{carpeta_destino}'")
                movido = True
                break
        
        # 4. Si no coincidió con nada, va a 'Otros'.
        if not movido:
            ruta_otros = os.path.join(downloads_path, 'Otros')
            shutil.move(ruta_archivo_origen, ruta_otros)
            print(f" -> Moviendo '{nombre_archivo}' a 'Otros'")

print("\n¡Organización completada con éxito! ✅")
