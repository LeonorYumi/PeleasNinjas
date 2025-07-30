class HabilidadNodo:
    def __init__(self, nombre, bono, hijos=None):
        self.nombre = nombre
        self.bono = bono
        self.hijos = hijos if hijos else []
    def bono_total(self):
        total = self.bono
        for hijo in self.hijos:
            total += hijo.bono_total()
        return total
    
habilidades_arbol = {
    "Fuego": HabilidadNodo("Fuego", 5, [
        HabilidadNodo("Llama Ardiente", 3),
        HabilidadNodo("Explosión de Ceniza", 2)
    ]),
    "Agua": HabilidadNodo("Agua", 4, [
        HabilidadNodo("Torrente", 3),
        HabilidadNodo("Maremoto", 4)
    ]),
    "Rayo": HabilidadNodo("Rayo", 6, [
        HabilidadNodo("Electroshock", 4),
        HabilidadNodo("Descarga rápida", 3)
    ]),
    "Especial": HabilidadNodo("Especial", 8),
}

def bono_habilidad(nombre_habilidad):
    nodo = habilidades_arbol.get(nombre_habilidad)
    if nodo:
        return nodo.bono_total()
    return 0

