def buscar_ninja_por_id_en_lista(ninjas, id_buscar):
    for n in ninjas:
        if n["id"] == id_buscar:
            return n
    return None

def buscar_ninja_por_id_en_archivo(id_buscar, archivo="ninjas.txt"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) < 6:
                    continue
                if datos[0] == id_buscar:
                    return {
                        "id": datos[0],
                        "nombre": datos[1],
                        "fuerza": int(datos[2]),
                        "agilidad": int(datos[3]),
                        "resistencia": int(datos[4]),
                        "habilidad": datos[5]
                    }
    except FileNotFoundError:
        print("Archivo de ninjas no encontrado.")
    return None
