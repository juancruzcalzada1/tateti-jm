def mostrar_tablero(tablero): # se crea función para crear el tablero e imprimirlo en pantalla
    for fila in tablero:
        for i in range (len (fila)): # recorre cada elemento de la fila
            if i==len(fila)-1: # representa el último elemento de cada lista,ya que el largo de cada sublista es de 5 elementos(len=4),ya que se cuenta desde subindice 0 a 4.
                print(fila[i],end='\n') # se muestra en pantalla sólo el último elemento de cada lista y con '\n' se baja al siguiente renglón, para armar el tablero
            else: # si no es el último elemento, se lo imprime en pantalla y no se baja a siguiente renglón
                print(fila[i], end='  ') 
tablero= [ 
    [' ', '|', ' ', '|', ' '], # posición 0,1,2,3,4 de la lista 0 [0:0,0:1,0:2,0:3,0:4]
    ['-', '+', '-', '+', '-'], # posición 0,1,2,3,4 de la lista 1 [1:0,1:1,1:2,1:3,1:4]
    [' ', '|', ' ', '|', ' '], # posición 0,1,2,3,4 de la lista 2 [2:0,2:1,2:2,2:3,2:4]
    ['-', '+', '-', '+', '-'], # posición 0,1,2,3,4 de la lista 3 [3:0,3:1,3:2,3:3,3:4]
    [' ', '|', ' ', '|', ' ']  # posición 0,1,2,3,4 de la lista 4 [4:0,4:1,4:2,4:3,4:4]
]
mostrar_tablero(tablero) # llama a la función para que se ejecute

jugador_1=str(input('ingrese su nombre: '))
jugador_2=str(input('ingrese su nombre: '))

'''import random  MIRKO NO FUNCIONA EL RANDOM
turno= random.randint(jugador_1,jugador_2)''' # Elige aleatoriamente quien comienza, si comienza el jugador_1,éste utiliza la X, sino, el jugador_2 comienza jugando con X; lo menciona el enunciado.
turno=true # variable que indica de quien es el turno de uno de los dos jugadores, al principio es del primer jugador y despues cambiarácon un not true o sea con false
letra_jugador_1=print('Ingrese por favor la letra con la que comienza el juego:')
letra_jugador_1=str(input('')) # para que el jugador que comienza ingrese la letra x
cantidad_de_jugadas=0 # contador de jugadas en una partida, se inicializa en 0, es decir, todavía no jugó nadie

while cantidad_de_jugadas<9 '''and letra_jugador_1!='x' and letra_jugador_1!='X' and letra_jugador_2!='o' and letra_jugador_2!='O' REACOMODAR YA QUE AL JUJADOR_1 LE PUEDE TOCAR LA OTRA LETRA''' # en total son 9 jugadas como máximo, pero como se cuenta desde el índice 0, son en total 8, es decir, se juega hasta 8 jugadas como máximo, cuando quiere pasar a 9 el programa se corta
    
    if letra_jugador_1=='x' or 'X':
        print(jugador_1,'elige una posición indicando el número de 0 a 9') # 0,1,2 es la primer fila del tablero;3,4,5 es la segunda fila mientras que, 6,7,8 es la tercera y última fila.
        jugada=int(input())
    else: # es decir, si el jugador 2 es el que comienza con la letra x, es el que arranca a jugar
       print(jugador_2,'elige una posición indicando el número de 0 a 9')
       jugada=int(input())
       
       valor=cambia_tablero(tablero, jugada, turno) # llama a la función cambia_tablero para que se ejecute
       if valor==0: # hace referencia al valor 0 del return
           print('corre bien la función cambia_tablero, siendo que la casilla no está todavía ocupada')
       else:
            print ('corre bien la función cambia_tablero, esta posición ya está ocupada')
       
def cambia_tablero(tablero,posición, jugador):# función que va cambiando el tablero a medida que van jugando
    if jugador_1==true: # si comienza el jugador_1 juega con x sino jugará luego de jugador 2 con 'o'
        simbolo='x'or 'X'
    else:
        simbolo='o' or 'O'
    if posición=1: # Hace referencia a la primer jugada, como máximo son 9 jugadas en una partida
        if tablero [4][0]='':   # si la posición 4:0 está vacía se juega
            tablero[4][0]=simbolo   # se completa tablero con el la x o la o
            return 0 # si devuelve 1 es que la función esta corriendo correctamente
        else:
            print ('esta posición ya está ocupada')
            
    elif posición=2:
        if tablero [4][2]='':   
            tablero[4][2]=simbolo   
            return 0
        else:
            print ('esta posición ya está ocupada')
            
     elif posición=3:
        if tablero [4][4]='':   
            tablero[4][4]=simbolo   
            return 0
        else:
            print ('esta posición ya está ocupada')
            
     elif posición=4:
        if tablero [2][0]='':   
            tablero[2][0]=simbolo   
            return 0
        else:
            print ('esta posición ya está ocupada')
            
     elif posición=5:
        if tablero [2][2]='':   
            tablero[2][2]=simbolo   
            return 0
        else:
            print ('esta posición ya está ocupada')
            
     elif posición=6:
        if tablero [2][4]='':   
            tablero[2][4]=simbolo   
            return 0
        else:
            print ('esta posición ya está ocupada')
            
     elif posición=7:
        if tablero [0][0]='':   
            tablero[0][0]=simbolo   
            return 0
        else:
            print ('esta posición ya está ocupada')
            
     elif posición=8:
        if tablero [0][2]='':   
            tablero[0][2]=simbolo   
            return 0
        else:
            print ('esta posición ya está ocupada')
            
     elif posición=9:
        if tablero [0][4]='':   
            tablero[0][4]=simbolo   
            return 0
        else:
            print ('esta posición ya está ocupada')
        
        posición=int(input)
        valor==cambia_tablero(tablero,posición, jugador)
        if valor==0: # si el valor del return es igual a 0 indica que la casilla se puede ocupar y que debe jugar el otro jugador
            turno=not true #sirve para que juegue el otro jugador, ya que el jugador que jugó recién tiene el valor booleano true
            cantidad_de_jugadas=cantidad_de_jugadas+1 # aumenta en  de uno en uno cada vez que va jugando un jugador
            mostrar_tablero(tablero) # Muestra como va quedando el tablero a medida que se va jugando          
            
        def ganador(tablero) #solo se necesita ver como quedó el tablera para saber quien gana
            for simbolo in ['x', 'X', 'o', 'O']
                fila_0=tablero[0][0]==simbolo and tablero[0][2]==simbolo and tablero[0][4]==simbolo
                fila_2=tablero[2][0]==simbolo and tablero[2][2]==simbolo and tablero[2][4]==simbolo
                fila_4=tablero[4][0]==simbolo and tablero[4][2]==simbolo and tablero[4][4]==simbolo
                columna_0=tablero[0][0]==simbolo and tablero[2][0]==simbolo and tablero[4][0]==simbolo
                columna_2=tablero[0][2]==simbolo and tablero[2][2]==simbolo and tablero[4][2]==simbolo
                columna_4=tablero[0][4]==simbolo and tablero[2][4]==simbolo and tablero[4][4]==simbolo
                diagonal_primaria=tablero[0][0]==simbolo and tablero[2][2]==simbolo and tablero[4][4]==simbolo
                diagonal_secundaria=tablero[4][0]==simbolo and tablero[2][2]==simbolo and tablero[0][4]==simbolo
                
                if fila_0 or fila_2 or fila_4 or columna_0 or columna_2 or columna_4 or diagonal_primaria or diagonal_secundaria:
                    if simbolo=='x':
                        print('el ganador es:', jugador_1) '''fijarse porque no se quien tiene la x'''
                    else:
                         print('el ganador es:', jugador_2)
                    break # si se cumple lo anterior ya hay ganador y no se vuelve a repetir el bucle for
                

         
           
        
        
       
       





