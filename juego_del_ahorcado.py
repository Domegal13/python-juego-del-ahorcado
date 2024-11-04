import random
from colorama import init, Fore, Back, Style
init()


def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'java', 'angular', 'react', 'typescript', 'git', 'tensorflow', 'flask',  'html', 'css', 'node', 'github', 'php', 'visual', 'sql', 'astro', 'pandas', 'cobol',  'basic']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"        

    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print('¡Bienvenido al juego del Ahorcado!')
    print(f'Tenés {intentos} intentos para adivinar la palabra secreta')
    print(mostrar_progreso(palabra_secreta, letras_adivinadas))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduce una letra válida")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra letra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                intentos -= 1
                print(f"Felicidades has acertado, la letra '{adivinanza}' está presente en la palabra")
                print(f"Te quedan {intentos} intentos")
            else:
                intentos -= 1
                print(f"Lo siento mucho la letra '{adivinanza}' no está presente en la palabra")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(Fore.LIGHTGREEN_EX + f"¡Felicidades has ganado! La palabra completa es: " + Fore.LIGHTYELLOW_EX + f"'{palabra_secreta.capitalize()}'" + Style.RESET_ALL)

    if intentos == 0 and not juego_terminado:
        print(Fore.LIGHTRED_EX + f"Lo sentimos mucho se te han acabado los intentos, la palabra secreta era: " + Fore.LIGHTYELLOW_EX + f"'{palabra_secreta.capitalize()}'")


if __name__ == "__main__":
    juego_ahorcado()
    




