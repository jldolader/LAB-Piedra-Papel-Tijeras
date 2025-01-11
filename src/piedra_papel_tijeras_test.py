from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    '''
    Test para la función ordenador_decide_jugada.
    '''
    print("Testeando ordenador_decide_jugada...")
    for _ in range(3):
        eleccion = ordenador_decide_jugada()
        print("El ordenador eligió:", eleccion)
    print("Test ordenador_decide_jugada completado.\n")

def test_usuario_decide_jugada():
    '''
    Test para la función usuario_decide_jugada.
    '''
    print("Testeando usuario_decide_jugada...")
    eleccion = usuario_decide_jugada()
    print("El usuario eligió:", eleccion)
    print("Test usuario_decide_jugada completado.\n")

def test_determina_ganador():
    '''
    Test para la función determina_ganador.
    '''
    print("Testeando determina_ganador...")
    escenarios = [
        ("piedra", "tijeras"),
        ("piedra", "papel"),
        ("piedra", "piedra"),
        ("tijeras", "papel"),
        ("tijeras", "piedra"),
        ("tijeras", "tijeras"),
        ("papel", "piedra"),
        ("papel", "tijeras"),
        ("papel", "papel"),
    ]

    for jugador, ordenador in escenarios:
        resultado = determina_ganador(jugador, ordenador)
        print(f"Jugador: {jugador}, Ordenador: {ordenador} -> Resultado: {resultado}")

    print("Test determina_ganador completado.\n")

def test_jugar():
    '''
    Test para la función jugar.
    '''
    print("Testeando jugar...")
    jugar()
    print("Test jugar completado.\n")

def test_jugar_torneo():
    '''
    Test para la función jugar_torneo.
    '''
    print("Testeando jugar_torneo...")
    jugar_torneo()
    print("Test jugar_torneo completado.\n")

# Función principal
if __name__ == "__main__":
    test_ordenador_decide_jugada()
    # test_usuario_decide_jugada()  # Este test requiere interacción del usuario, descomentar para probar
    test_determina_ganador()
    test_jugar()
    test_jugar_torneo()