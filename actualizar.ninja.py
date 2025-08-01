def actualizar_ninja(ninjas):
    id = input("ID del ninja a actualizar: ")
    ninja = buscar_ninja_por_id_en_lista(ninjas, id)
    if not ninja:
        print("Ninja no encontrado.")
        return
    nombre = input(f"Nuevo nombre (Enter para mantener {ninja['nombre']}): ")
    if nombre.strip():
        ninja["nombre"] = nombre
    try:
        fuerza = input(f"Fuerza (Enter para mantener {ninja['fuerza']}): ")
        if fuerza.strip():
            ninja["fuerza"] = int(fuerza)
        agilidad = input(f"Agilidad (Enter para mantener {ninja['agilidad']}): ")
        if agilidad.strip():
            ninja["agilidad"] = int(agilidad)
        resistencia = input(f"Resistencia (Enter para mantener {ninja['resistencia']}): ")
        if resistencia.strip():
            ninja["resistencia"] = int(resistencia)
    except ValueError:
        print("Valor inválido. No se actualizó ese campo.")
    print("Habilidades disponibles:")
    for hab in habilidades_arbol.keys():
        print(f"- {hab}")
    habilidad = input(f"Habilidad (Enter para mantener {ninja['habilidad']}): ")
    if habilidad.strip():
        if habilidad in habilidades_arbol:
            ninja["habilidad"] = habilidad
        else:
            print("Habilidad no válida, se mantiene la anterior.")
    print("Ninja actualizado.")
