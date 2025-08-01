import random                  
from collections import deque  
from datetime import datetime   

#CLASES
class NodoHabilidad:
    def __init__(self, nombre, bono):
        self.nombre = nombre
        self.bono = bono
        self.izquierda = None
        self.derecha = None

    def bono_total(self):
        total = self.bono
        if self.izquierda:
            total += self.izquierda.bono_total()
        if self.derecha:
            total += self.derecha.bono_total()
        return total

    def preorden(self):
        res = [self.nombre]
        if self.izquierda:
            res.extend(self.izquierda.preorden())
        if self.derecha:
            res.extend(self.derecha.preorden())
        return res

    def inorden(self):
        res = []
        if self.izquierda:
            res.extend(self.izquierda.inorden())
        res.append(self.nombre)
        if self.derecha:
            res.extend(self.derecha.inorden())
        return res

    def postorden(self):
        res = []
        if self.izquierda:
            res.extend(self.izquierda.postorden())
        if self.derecha:
            res.extend(self.derecha.postorden())
        res.append(self.nombre)
        return res

# --- FUNCIONES HABILIDADES ---

def cargar_arbol_habilidades(id_ninja, archivo="habilidades_ninjas.txt"):
    
    habilidades = {}
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for line in f:
                partes = line.strip().split(",")
                if len(partes) != 5:
                    continue
                nid, nombre, bono, izq, der = partes
                if nid != id_ninja:
                    continue
                bono = int(bono)
                habilidades[nombre] = {"bono": bono, "izq": izq if izq != "None" else None, "der": der if der != "None" else None}
    except FileNotFoundError:
        return None

    # Armar árbol recursivamente
    def crear_nodo(nombre):
        if nombre is None or nombre not in habilidades:
            return None
        info = habilidades[nombre]
        nodo = NodoHabilidad(nombre, info["bono"])
        nodo.izquierda = crear_nodo(info["izq"])
        nodo.derecha = crear_nodo(info["der"])
        return nodo

    # Encontrar la raíz (la que aparece como clave pero no en izq ni der)
    nodos_hijos = set()
    for v in habilidades.values():
        if v["izq"]:
            nodos_hijos.add(v["izq"])
        if v["der"]:
            nodos_hijos.add(v["der"])
    raiz_nombre = None
    for clave in habilidades.keys():
        if clave not in nodos_hijos:
            raiz_nombre = clave
            break
    if raiz_nombre is None:
        return None
    return crear_nodo(raiz_nombre)

# FUNCIONES USUARIOS 

def validar_correo(correo):
    partes = correo.split("@")
    if len(partes) != 2:
        return False
    usuario, dominio = partes
    if dominio != "gmail.com":
        return False
    if "." not in usuario:
        return False
    return True

def validar_contraseña(contra):
    return (len(contra) >= 8 and
            any(c.isupper() for c in contra) and
            any(c.isdigit() for c in contra))

def solo_letras(nombre_y_apellido):
    return all(c.isalpha() or c.isspace() for c in nombre_y_apellido) and nombre_y_apellido.strip() != ""

def identificacion_existente(identificacion):
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 4 and partes[3] == identificacion:
                    return True
    except FileNotFoundError:
        return False
    return False

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    while True:
        nombre = input("Nombres y Apellidos: ")
        if solo_letras(nombre):
            break
        else:
            print("Error: Solo letras y espacios.")
    while True:
        identificacion = input("Identificación (10 dígitos): ")
        if identificacion.isdigit() and len(identificacion) == 10:
            if not identificacion_existente(identificacion):
                break
            else:
                print("ID ya registrado.")
        else:
            print("Error: ID debe ser 10 dígitos.")
    while True:
        edad = input("Edad: ")
        if edad.isdigit() and int(edad) > 0:
            break
        else:
            print("Edad inválida.")
    while True:
        usuario = input("Correo (nombre.apellido@gmail.com): ")
        if validar_correo(usuario):
            break
        else:
            print("Correo inválido.")
    while True:
        contra = input("Contraseña (mín 8 caracteres, 1 mayúscula, 1 número): ")
        if validar_contraseña(contra):
            break
        else:
            print("Contraseña no segura.")
    with open("usuarios.txt", "a", encoding="utf-8") as f:
        f.write(f"{usuario},{contra},{nombre},{identificacion},{edad}\n")
    print("Usuario registrado exitosamente.")

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    usuario = input("Correo: ")
    contra = input("Contraseña: ")
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 2 and partes[0] == usuario and partes[1] == contra:
                    print(f"Bienvenido {partes[2]}!")
                    return usuario
    except FileNotFoundError:
        pass
    print("Credenciales incorrectas.")
    return None

# --- FUNCIONES NINJAS ---

def cargar_ninjas(archivo="ninjas.txt"):
    ninjas = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) < 8:
                    continue
                ninjas.append({
                    "id": partes[0],
                    "nombre": partes[1],
                    "fuerza": int(partes[2]),
                    "agilidad": int(partes[3]),
                    "resistencia": int(partes[4]),
                    "habilidad": partes[5],
                    "puntos": int(partes[6]),
                    "email_dueño": partes[7]
                })
    except FileNotFoundError:
        pass
    return ninjas