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

def crear_ninja(ninjas):
    id = input("Nuevo ID: ")
    if buscar_ninja_por_id_en_lista(ninjas, id):
        print("ID ya existe.")
        return
    nombre = input("Nombre del ninja: ")
    fuerza = random.randint(5, 10)
    agilidad = random.randint(5, 10)
    resistencia = random.randint(5, 10)

    print("Habilidades disponibles:")
    for hab in habilidades_arbol.keys():
        print(f"- {hab}")
    habilidad = input("Elige la habilidad: ")
    if habilidad not in habilidades_arbol:
        print("Habilidad no válida. Se asignará 'Especial' por defecto.")
        habilidad = "Especial"

    ninjas.append({
        "id": id,
        "nombre": nombre,
        "fuerza": fuerza,
        "agilidad": agilidad,
        "resistencia": resistencia,
        "habilidad": habilidad
    })
    print("Ninja creado con atributos aleatorios y habilidad asignada.")