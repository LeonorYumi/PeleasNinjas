def cargar_ninjas(archivo="ninjas.txt"):
    ninjas = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) < 6:
                    continue
                ninjas.append({
                    "id": datos[0],
                    "nombre": datos[1],
                    "fuerza": int(datos[2]),
                    "agilidad": int(datos[3]),
                    "resistencia": int(datos[4]),
                    "habilidad": datos[5]
                })
    except FileNotFoundError:
        pass
    return ninjas