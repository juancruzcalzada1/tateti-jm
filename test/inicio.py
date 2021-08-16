#Función de inicio - Define de forma aleatoria quien es "X" e "O" y quien comienza jugando en la partida.
import random

simbolos=["X","O"]

jug1=str(input('Ingresar nombre del jugador 1: '))
jug2=str(input('Ingresar nombre del jugador 2: '))

def ini_partida(x,y):
    jugadores=[jug1,jug2]
    asig1=(random.choice(simbolos))
    if asig1=='X':
        asig2='O'
    else:
        asig2='X'
    print('La asignación de letras es: ', jug1,'=',asig1, '|', jug2, '=', asig2)
    print('Inicia la partida:',random.choice(jugadores))
    return ()

ini_partida(jug1,jug2)




