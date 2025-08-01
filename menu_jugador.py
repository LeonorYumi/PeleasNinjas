def menu_jugador(ninjas, email_usuario):
    while True:
        print("\n--- Menú Jugador ---")
        print("1. 🌲 Ver árbol de habilidades ninja")
        print("2. ⚔️ Simular combate 1 vs 1")
        print("3. 🤺 Simular torneo completo")
        print("4. 🛡️ Consultar ranking")
        print("5. 🔎 Buscar ninja")
        print("6. ⬅️ Salir")
        opcion = input("Elige opción: ")
        if opcion == "1":
            ver_arbol_habilidades(ninjas)
        elif opcion == "2":
            combate_1vs1(ninjas)
        elif opcion == "3":
            torneo_completo(ninjas)
        elif opcion == "4":
            mostrar_ranking(ninjas)
        elif opcion == "5":
            buscar_ninja_menu(ninjas)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

def ver_arbol_habilidades(ninjas):
    id_n = input("ID ninja para ver árbol: ")
    arbol = cargar_arbol_habilidades(id_n)
    if arbol is None:
        print("No tiene árbol de habilidades.")
        return
    print("Recorrido Preorden:", arbol.preorden())
    print("Recorrido Inorden:", arbol.inorden())
    print("Recorrido Postorden:", arbol.postorden())

def combate_1vs1(ninjas):
    id1 = input("ID Ninja 1: ")
    id2 = input("ID Ninja 2: ")
    n1 = buscar_ninja_por_id(ninjas, id1)
    n2 = buscar_ninja_por_id(ninjas, id2)
    if not n1 or not n2:
        print("Ninja(s) no encontrados.")
        return
    arbol1 = cargar_arbol_habilidades(n1['id'])
    arbol2 = cargar_arbol_habilidades(n2['id'])
    habilidades_dict = {}  # Para simplificar: sin bonos detallados
    ganador = pelea(n1, n2, habilidades_dict, arbol1, arbol2)
    print(f"Ganador: {ganador['nombre']}")
    ganador['puntos'] += 1
    guardar_historial_combate(n1, n2, ganador)
    guardar_ninjas(ninjas)

def torneo_completo(ninjas):
    if len(ninjas) < 2:
        print("No hay suficientes ninjas.")
        return
    habilidades_dict = {}
    campeon = torneo(ninjas, habilidades_dict)
    print(f"Campeón: {campeon['nombre']}")
    guardar_ninjas(ninjas)

# --- PROGRAMA PRINCIPAL ---

def main():
    ninjas = cargar_ninjas()
    print("========== 🥷Bienvenido a PoliNinjaGames🥷 ===========")
    while True:
        print("\n1. Registrar usuario\n2. Iniciar sesión\n3. Salir")
        op = input("Opción: ")
        if op == "1":
            registrar_usuario()
        elif op == "2":
            usuario = iniciar_sesion()
            if usuario:
                if usuario == "admin@gmail.com":
                    menu_admin(ninjas)
                else:
                    menu_jugador(ninjas, usuario)
        elif op == "3":
            print("Hasta pronto!😊")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
