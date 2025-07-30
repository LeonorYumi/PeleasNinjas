def eliminar_ninja(ninjas):
    id = input("ID del ninja a eliminar: ")
    ninja = buscar_ninja_por_id_en_lista(ninjas, id)
    if ninja:
        ninjas.remove(ninja)
        print(f"Ninja {ninja['nombre']} eliminado.")
    else:
        print("Ninja no encontrado.")
