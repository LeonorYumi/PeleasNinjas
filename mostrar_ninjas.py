def mostrar_ninjas(ninjas):
    if not ninjas:
        print("No hay ninjas registrados.")
        return
    for n in ninjas:
        print(f"ID: {n['id']} - Nombre: {n['nombre']} - Fuerza: {n['fuerza']} - Agilidad: {n['agilidad']} - Resistencia: {n['resistencia']} - Habilidad: {n['habilidad']}")
