def pelea(ninja1, ninja2):
    puntaje1 = (ninja1['fuerza'] * 2 +
                ninja1['agilidad'] * 1.5 +
                ninja1['resistencia'] +
                bono_habilidad(ninja1['habilidad']))
    puntaje2 = (ninja2['fuerza'] * 2 +
                ninja2['agilidad'] * 1.5 +
                ninja2['resistencia'] +
                bono_habilidad(ninja2['habilidad']))
    puntaje1 += random.uniform(-2, 2)
    puntaje2 += random.uniform(-2, 2)
    print(f"{ninja1['nombre']} puntaje total: {puntaje1:.2f}")
    print(f"{ninja2['nombre']} puntaje total: {puntaje2:.2f}")
    if puntaje1 > puntaje2:
        return ninja1
    elif puntaje2 > puntaje1:
        return ninja2
    else:
        return random.choice([ninja1, ninja2])
