import os
import shutil
import datetime

# --- RUTA REAL PARA ANDROID ---
downloads_path = '/data/data/com.termux/files/home/storage/shared/Download'

# --- RUTA PARA EL ARCHIVO DE LOG (se creará en la carpeta de Descargas) ---
log_file_path = os.path.join(downloads_path, 'organizador_log.txt')

# --- FUNCIÓN PARA ESCRIBIR EN EL LOG ---
def registrar_accion(mensaje):
    """Añade un mensaje con fecha y hora al archivo de log."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"[{timestamp}] {mensaje}\n")

# --- ESTRUCTURA DE CARPETAS ---
carpetas_principales = {
    'Camara y WhatsApp': [],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.webm'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.xlsm', '.csv'],
    'Musica': ['.mp3', '.wav', '.opus', '.m4a'],
    'Comprimidos': ['.zip', '.rar'],
    'Apps y Ejecutables': ['.apk', '.exe', '.zip'],
    'Otros': []
}

# --- INICIO DEL SCRIPT ---
registrar_accion("--- INICIO DEL PROCESO DE ORGANIZACIÓN ---")
print("Verificando estructura de carpetas...")
# (El resto del código sigue igual, pero ahora usa la función registrar_accion)
for carpeta in carpetas_principales.keys():
    ruta_carpeta = os.path.join(downloads_path, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

ruta_camara_whatsapp = os.path.join(downloads_path, 'Camara y WhatsApp')
subcarpetas_camara = ['Fotos', 'Videos']
for subcarpeta in subcarpetas_camara:
    ruta_subcarpeta = os.path.join(ruta_camara_whatsapp, subcarpeta)
    if not os.path.exists(ruta_subcarpeta):
        os.makedirs(ruta_subcarpeta)

print("\n✅ ¡Todo listo! Iniciando organización de archivos...")

for nombre_archivo in os.listdir(downloads_path):
    ruta_archivo_origen = os.path.join(downloads_path, nombre_archivo)

    if os.path.isfile(ruta_archivo_origen):
        
        # Ignorar el propio archivo de log para que no se mueva a sí mismo
        if nombre_archivo == 'organizador_log.txt':
            continue

        movido = False
        
        # Reglas para la cámara y WhatsApp
        if nombre_archivo.startswith('IMG_') or nombre_archivo.startswith('IMG-'):
            ruta_destino = os.path.join(ruta_camara_whatsapp, 'Fotos')
            mensaje_log = f"MOVIDO a 'Camara y WhatsApp/Fotos': {nombre_archivo}"
            registrar_accion(mensaje_log)
            print(f"📸 {mensaje_log}")
            shutil.move(ruta_archivo_origen, ruta_destino)
            movido = True

        elif nombre_archivo.startswith('VID_') or nombre_archivo.startswith('VID-'):
            ruta_destino = os.path.join(ruta_camara_whatsapp, 'Videos')
            mensaje_log = f"MOVIDO a 'Camara y WhatsApp/Videos': {nombre_archivo}"
            registrar_accion(mensaje_log)
            print(f"📹 {mensaje_log}")
            shutil.move(ruta_archivo_origen, ruta_destino)
            movido = True

        # Lógica para el resto de archivos
        if not movido:
            extension = os.path.splitext(nombre_archivo)[1].lower()
            for carpeta_destino, extensiones_validas in carpetas_principales.items():
                if carpeta_destino == 'Camara y WhatsApp':
                    continue
                
                if extension in extensiones_validas:
                    ruta_carpeta_destino = os.path.join(downloads_path, carpeta_destino)
                    mensaje_log = f"MOVIDO a '{carpeta_destino}': {nombre_archivo}"
                    registrar_accion(mensaje_log)
                    print(f" -> {mensaje_log}")
                    shutil.move(ruta_archivo_origen, ruta_carpeta_destino)
                    movido = True
                    break
        
        if not movido:
            ruta_otros = os.path.join(downloads_path, 'Otros')
            mensaje_log = f"MOVIDO a 'Otros': {nombre_archivo}"
            registrar_accion(mensaje_log)
            print(f" -> {mensaje_log}")
            shutil.move(ruta_archivo_origen, ruta_otros)

registrar_accion("--- FIN DEL PROCESO DE ORGANIZACIÓN ---")
print(f"\n¡Organización completada! ✅\n📝 Se ha creado un registro de todas las acciones en el archivo: organizador_log.txt")
