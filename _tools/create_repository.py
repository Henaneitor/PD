import os
import hashlib

# Configuración
root_path = '../zips/'
output_xml = '../zips/addons.xml'
output_md5 = '../zips/addons.xml.md5'

def generate_repo():
    xml_content = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n'
    
    # Busca en cada carpeta de zips
    for folder in os.listdir(root_path):
        folder_path = os.path.join(root_path, folder)
        if os.path.isdir(folder_path):
            # Busca el addon.xml suelto
            xml_file = os.path.join(folder_path, 'addon.xml')
            if os.path.exists(xml_file):
                with open(xml_file, 'r', encoding='utf-8') as f:
                    # Se salta la cabecera y añade el cuerpo
                    lines = f.readlines()
                    for line in lines:
                        if '<?xml' not in line:
                            xml_content += line
                    xml_content += '\n'

    xml_content += '</addons>'
    
    # Escribir el addons.xml gigante
    with open(output_xml, 'w', encoding='utf-8') as f:
        f.write(xml_content)
        
    # Generar el MD5 (Vital para Kodi)
    md5 = hashlib.md5(xml_content.encode('utf-8')).hexdigest()
    with open(output_md5, 'w', encoding='utf-8') as f:
        f.write(md5)
        
    print("Repositorio generado correctamente en /zips/")

if __name__ == '__main__':
    generate_repo()