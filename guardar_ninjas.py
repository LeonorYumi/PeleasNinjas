
def guardar_ninjas(ninjas, archivo="ninjas.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        for n in ninjas:
            f.write(f"{n['id']},{n['nombre']},{n['fuerza']},{n['agilidad']},{n['resistencia']},{n['habilidad']}\n")
