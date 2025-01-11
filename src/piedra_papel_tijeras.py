import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ").lower()
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif (jugada_usuario == "piedra" and jugada_ordenador == "tijeras") or \
         (jugada_usuario == "tijeras" and jugada_ordenador == "papel") or \
         (jugada_usuario == "papel" and jugada_ordenador == "piedra"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    print("\n🎮 Nueva Ronda 🎮")
    jugada_usuario = usuario_decide_jugada()
    jugada_ordenador = ordenador_decide_jugada()
    print(f"\nEl ordenador ha escogido: {jugada_ordenador}")
    resultado = determina_ganador(jugada_usuario, jugada_ordenador)
    
    if resultado == "Empate":
        print("🤝 ¡Empate!")
    elif resultado == "Ganaste":
        print("✅ ¡Ganaste esta ronda!")
    else:
        print("❌ ¡Perdiste esta ronda!")
    
    return resultado

def jugar_torneo():
    print("🏆 ¡Bienvenido al torneo de Piedra, Papel o Tijeras! 🏆")
    puntos_usuario, puntos_ordenador = 0, 0

    while puntos_usuario < 3 and puntos_ordenador < 3:
        resultado_ronda = jugar()
        
        if resultado_ronda == "Ganaste":
            puntos_usuario += 1
        elif resultado_ronda == "Perdiste":
            puntos_ordenador += 1

        print(f"\nPuntaje -> Usuario: {puntos_usuario} | Ordenador: {puntos_ordenador}")
        print("-" * 40)

    print("\n" + "=" * 40)
    if puntos_usuario == 3:
        print("🎉 ¡Felicidades, ganaste el torneo! 🎉")
    else:
        print("💻 El ordenador ganó el torneo. ¡Suerte la próxima vez! 💻")

if __name__ == "__main__":
    jugar_torneo()