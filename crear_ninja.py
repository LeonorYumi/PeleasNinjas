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