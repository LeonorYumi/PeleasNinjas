def guardar_ninjas(ninjas, archivo="ninjas.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        for n in ninjas:
            f.write(f"{n['id']},{n['nombre']},{n['fuerza']},{n['agilidad']},{n['resistencia']},{n['habilidad']},{n['puntos']},{n['email_dueño']}\n")

def buscar_ninja_por_id(ninjas, id_buscar):
    for n in ninjas:
        if n["id"] == id_buscar:
            return n
    return None

def buscar_ninja_por_nombre(ninjas, nombre_buscar):
    for n in ninjas:
        if n["nombre"].lower() == nombre_buscar.lower():
            return n
    return None

def quicksort_ninjas(ninjas, key, inicio=0, fin=None):
    if fin is None:
        fin = len(ninjas) - 1
    if inicio < fin:
        pi = particion(ninjas, key, inicio, fin)
        quicksort_ninjas(ninjas, key, inicio, pi-1)
        quicksort_ninjas(ninjas, key, pi+1, fin)

def particion(arr, key, low, high):
    pivot = arr[high][key]
    i = low -1
    for j in range(low, high):
        if arr[j][key] >= pivot:  # ordenar descendente
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

# --- FUNCIONES COMBATE ---

def elegir_estrategia(nodo_raiz, estado_combate):
    # Retorna lista de técnicas según recorrido del árbol de habilidades
    if nodo_raiz is None:
        return []
    if estado_combate == "ganando":
        return nodo_raiz.preorden()
    elif estado_combate == "empatado":
        return nodo_raiz.inorden()
    else:
        return nodo_raiz.postorden()

def bono_estrategia(nombre_tecnica, habilidades_dict):
    # Suma el bono de la técnica y sus subnodos (simulación)
    # Aquí se asume que el bono de la técnica es fijo (por simplicidad)
    # Si quieres, puedes refinar esto.
    if nombre_tecnica in habilidades_dict:
        return habilidades_dict[nombre_tecnica]
    return 0

def pelea(ninja1, ninja2, habilidades_dict, arbol1, arbol2):
    # Se simula un combate usando atributos + árbol + random
    # Se calcula puntaje base:
    puntaje1 = (ninja1['fuerza'] * 2 +
                ninja1['agilidad'] * 1.5 +
                ninja1['resistencia'])
    puntaje2 = (ninja2['fuerza'] * 2 +
                ninja2['agilidad'] * 1.5 +
                ninja2['resistencia'])

    # Estado inicial empate
    estado = "empatado"

    # Elegir estrategia técnica para cada ninja
    tecnicas1 = elegir_estrategia(arbol1, estado)
    tecnicas2 = elegir_estrategia(arbol2, estado)

    # Seleccionar técnica aleatoria de la lista
    if tecnicas1:
        tecnica1 = random.choice(tecnicas1)
    else:
        tecnica1 = None
    if tecnicas2:
        tecnica2 = random.choice(tecnicas2)
    else:
        tecnica2 = None

    bono1 = bono_estrategia(tecnica1, habilidades_dict) if tecnica1 else 0
    bono2 = bono_estrategia(tecnica2, habilidades_dict) if tecnica2 else 0

    puntaje1 += bono1 + random.uniform(-2, 2)
    puntaje2 += bono2 + random.uniform(-2, 2)

    print(f"\n{ninja1['nombre']} usa {tecnica1} + bono {bono1:.2f}, puntaje total: {puntaje1:.2f}")
    print(f"{ninja2['nombre']} usa {tecnica2} + bono {bono2:.2f}, puntaje total: {puntaje2:.2f}")

    if puntaje1 > puntaje2:
        return ninja1
    elif puntaje2 > puntaje1:
        return ninja2
    else:
        # desempate aleatorio
        return random.choice([ninja1, ninja2])

# --- FUNCIONES TORNEO ---

def torneo(ninjas, habilidades_dict):
    # Usa cola para simular torneo con eliminacion simple y evitar repetir emparejamientos
    participantes = ninjas[:]
    random.shuffle(participantes)
    cola = deque(participantes)
    rondas_anteriores = set()
    ronda_num = 1

    while len(cola) > 1:
        print(f"\n--- Ronda {ronda_num} ---")
        siguiente_ronda = deque()
        enfrentados = set()
        while len(cola) > 0:
            n1 = cola.popleft()
            if len(cola) == 0:
                # pasa directo
                print(f"{n1['nombre']} pasa sin rival.")
                siguiente_ronda.append(n1)
                break
            n2 = cola.popleft()

            # Ver si ya pelearon esta ejecución (por ids concatenados)
            par = tuple(sorted([n1['id'], n2['id']]))
            if par in enfrentados:
                # ya peleados, se pasa n2 al final para evitar repetición
                cola.append(n2)
                # Se regresa n1 al inicio para esperar rival diferente
                cola.appendleft(n1)
                continue
            enfrentados.add(par)

            # Cargar árboles de habilidades
            arbol1 = cargar_arbol_habilidades(n1['id'])
            arbol2 = cargar_arbol_habilidades(n2['id'])

            ganador = pelea(n1, n2, habilidades_dict, arbol1, arbol2)
            print(f"Ganador: {ganador['nombre']}")
            ganador['puntos'] += 1  # sumar victoria

            guardar_historial_combate(n1, n2, ganador)
            siguiente_ronda.append(ganador)
        cola = siguiente_ronda
        ronda_num += 1

    print(f"\n*** Campeón del torneo: {cola[0]['nombre']} ***")
    return cola[0]

# --- HISTORIAL DE COMBATES ---

def guardar_historial_combate(n1, n2, ganador):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linea = f"{n1['nombre']} vs {n2['nombre']} - Ganador: {ganador['nombre']} - Fecha: {fecha}\n"
    with open("combates.txt", "a", encoding="utf-8") as f:
        f.write(linea)

def guardar_historial_usuario(email, ganados=0, perdidos=0):
    archivo = f"combates_usuario_{email}.txt"
    with open(archivo, "w", encoding="utf-8") as f:
        f.write(f"Ganados: {ganados}\nPerdidos: {perdidos}\n")

# --- RANKING ---

def mostrar_ranking(ninjas):
    if not ninjas:
        print("No hay ninjas.")
        return
    # Ordenar por puntos de victoria con QuickSort descendente
    quicksort_ninjas(ninjas, "puntos")
    print("\n--- Ranking de ninjas (por victorias) ---")
    for n in ninjas:
        print(f"ID: {n['id']} - {n['nombre']} - Victorias: {n['puntos']}")

# --- MENÚ ADMINISTRADOR ---

def menu_admin(ninjas):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Agregar ninja")
        print("2. Listar ninjas")
        print("3. Buscar ninja (ID o Nombre)")
        print("4. Actualizar ninja")
        print("5. Eliminar ninja")
        print("6. Guardar cambios")
        print("7. Salir")
        opcion = input("Elige opción: ")
        if opcion == "1":
            crear_ninja(ninjas)
        elif opcion == "2":
            mostrar_ninjas(ninjas)
        elif opcion == "3":
            buscar_ninja_menu(ninjas)
        elif opcion == "4":
            actualizar_ninja(ninjas)
        elif opcion == "5":
            eliminar_ninja(ninjas)
        elif opcion == "6":
            guardar_ninjas(ninjas)
            print("Cambios guardados.")
        elif opcion == "7":
            guardar_ninjas(ninjas)
            print("Saliendo de administrador.")
            break
        else:
            print("Opción inválida.")

# --- FUNCIONES CRUD NINJAS ADMIN ---

def crear_ninja(ninjas):
    id_n = input("ID nuevo ninja: ")
    if buscar_ninja_por_id(ninjas, id_n):
        print("ID ya existe.")
        return
    nombre = input("Nombre ninja: ")
    fuerza = random.randint(5,10)
    agilidad = random.randint(5,10)
    resistencia = random.randint(5,10)
    print("Habilidades disponibles: Fuego, Agua, Rayo, Especial")
    habilidad = input("Elige habilidad: ")
    if habilidad not in ["Fuego", "Agua", "Rayo", "Especial"]:
        print("Habilidad no válida, se asigna 'Especial'")
        habilidad = "Especial"
    ninjas.append({
        "id": id_n,
        "nombre": nombre,
        "fuerza": fuerza,
        "agilidad": agilidad,
        "resistencia": resistencia,
        "habilidad": habilidad,
        "puntos": 0,
        "email_dueño": "admin"
    })
    print(f"Ninja {nombre} creado.")

def mostrar_ninjas(ninjas):
    if not ninjas:
        print("No hay ninjas.")
        return
    for n in ninjas:
        print(f"ID: {n['id']} Nombre: {n['nombre']} Fuerza: {n['fuerza']} Agilidad: {n['agilidad']} Resistencia: {n['resistencia']} Habilidad: {n['habilidad']} Puntos: {n['puntos']}")

def buscar_ninja_menu(ninjas):
    criterio = input("Buscar por (1) ID o (2) Nombre? ")
    if criterio == "1":
        id_b = input("ID: ")
        ninja = buscar_ninja_por_id(ninjas, id_b)
        if ninja:
            print(ninja)
        else:
            print("Ninja no encontrado.")
    elif criterio == "2":
        nombre_b = input("Nombre: ")
        ninja = buscar_ninja_por_nombre(ninjas, nombre_b)
        if ninja:
            print(ninja)
        else:
            print("Ninja no encontrado.")
    else:
        print("Opción inválida.")

def actualizar_ninja(ninjas):
    id_n = input("ID ninja a actualizar: ")
    ninja = buscar_ninja_por_id(ninjas, id_n)
    if not ninja:
        print("Ninja no existe.")
        return
    print("Dejar vacío para no cambiar")
    nombre = input(f"Nombre ({ninja['nombre']}): ")
    if nombre != "":
        ninja['nombre'] = nombre
    # Actualizar atributos con validación
    for attr in ['fuerza','agilidad','resistencia']:
        valor = input(f"{attr.capitalize()} ({ninja[attr]}): ")
        if valor.isdigit():
            ninja[attr] = int(valor)
    habilidad = input(f"Habilidad ({ninja['habilidad']}): ")
    if habilidad != "":
        ninja['habilidad'] = habilidad
    print("Actualizado.")

def eliminar_ninja(ninjas):
    id_n = input("ID ninja a eliminar: ")
    ninja = buscar_ninja_por_id(ninjas, id_n)
    if not ninja:
        print("Ninja no existe.")
        return
    ninjas.remove(ninja)
    print("Ninja eliminado.")
