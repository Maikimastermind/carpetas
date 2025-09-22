import os
import shutil

# --- RUTA REAL PARA ANDROID ---
downloads_path = '/data/data/com.termux/files/home/storage/shared/Download'

# --- ESTRUCTURA DE CARPETAS MEJORADA ---
carpetas_principales = {
    'Camara y WhatsApp': [], # Un solo lugar para fotos/videos del teléfono
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.webm'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.xlsm', '.csv'],
    'Musica': ['.mp3', '.wav', '.opus', '.m4a'],
    'Comprimidos': ['.zip', '.rar'],
    'Apps y Ejecutables': ['.apk', '.exe', '.zip'], # El .zip está aquí por si son proyectos
    'Otros': []
}

# --- LÓGICA DEL SCRIPT FINAL ---

# Crear todas las carpetas principales si no existen
print("Verificando estructura de carpetas...")
for carpeta in carpetas_principales.keys():
    ruta_carpeta = os.path.join(downloads_path, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# Crear subcarpetas para fotos y videos de la cámara/whatsapp
ruta_camara_whatsapp = os.path.join(downloads_path, 'Camara y WhatsApp')
subcarpetas_camara = ['Fotos', 'Videos']
for subcarpeta in subcarpetas_camara:
    ruta_subcarpeta = os.path.join(ruta_camara_whatsapp, subcarpeta)
    if not os.path.exists(ruta_subcarpeta):
        os.makedirs(ruta_subcarpeta)

print("\n✅ ¡Todo listo! Iniciando organización de archivos...")

# Revisar cada archivo en la carpeta de Descargas.
for nombre_archivo in os.listdir(downloads_path):
    ruta_archivo_origen = os.path.join(downloads_path, nombre_archivo)

    if os.path.isfile(ruta_archivo_origen):
        
        # --- REGLAS MEJORADAS PARA FOTOS Y VIDEOS DEL TELÉFONO ---
        # Ahora reconoce IMG_ (cámara) y IMG- (WhatsApp)
        if nombre_archivo.startswith('IMG_') or nombre_archivo.startswith('IMG-'):
            ruta_destino = os.path.join(ruta_camara_whatsapp, 'Fotos')
            shutil.move(ruta_archivo_origen, ruta_destino)
            print(f"📸 Moviendo foto '{nombre_archivo}' a 'Camara y WhatsApp/Fotos'")
            continue

        # Ahora reconoce VID_ (cámara) y VID- (WhatsApp)
        if nombre_archivo.startswith('VID_') or nombre_archivo.startswith('VID-'):
            ruta_destino = os.path.join(ruta_camara_whatsapp, 'Videos')
            shutil.move(ruta_archivo_origen, ruta_destino)
            print(f"📹 Moviendo video '{nombre_archivo}' a 'Camara y WhatsApp/Videos'")
            continue

        # --- LÓGICA PARA EL RESTO DE ARCHIVOS ---
        extension = os.path.splitext(nombre_archivo)[1].lower()
        movido = False
        for carpeta_destino, extensiones_validas in carpetas_principales.items():
            if carpeta_destino == 'Camara y WhatsApp':
                continue
            
            if extension in extensiones_validas:
                ruta_carpeta_destino = os.path.join(downloads_path, carpeta_destino)
                shutil.move(ruta_archivo_origen, ruta_carpeta_destino)
                print(f" -> Moviendo '{nombre_archivo}' a '{carpeta_destino}'")
                movido = True
                break
        
        if not movido:
            ruta_otros = os.path.join(downloads_path, 'Otros')
            shutil.move(ruta_archivo_origen, ruta_otros)
            print(f" -> Moviendo '{nombre_archivo}' a 'Otros'")

print("\n¡Organización completada con éxito! Revisa tu carpeta de Descargas. ✨")
