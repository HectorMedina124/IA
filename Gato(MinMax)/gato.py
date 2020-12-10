import numpy as np
import random


def definirTablero():
    m=[[" "," "," "],[" "," "," ",],[" "," "," ",]]
    matriz=np.array(m)
    return matriz


def imprimirTablero(tablero):
    print("|-------|-------|-------|")
    print("|   "+tablero[0][0]+"   |   "+tablero[0][1]+"   |   "+tablero[0][2]+"   |")
    print("|-------|-------|-------|")
    print("|   "+tablero[1][0]+"   |   "+tablero[1][1]+"   |   "+tablero[1][2]+"   |")
    print("|-------|-------|-------|")
    print("|   "+tablero[2][0]+"   |   "+tablero[2][1]+"   |   "+tablero[2][2]+"   |")
    print("|-------|-------|-------|")


def empezarJuegoM():
    respuesta=3
    while(respuesta!=1 and respuesta!=2):
        respuesta=int(input("¿Quien desea que empieze el juego? Jugador=1,Maquina=2\n"))

    if(respuesta==1):
        jugador="El Jugador"
        simbolo="x"
    else:
        jugador=" La Maquina"
        simbolo="o"
    
    tablero=definirTablero()
    turno=1
    while(turno<=9):
        imprimirTablero(tablero)
        print("Turno de "+jugador)
        if(simbolo=="x"):
            print(agregar(simbolo,tablero))
            if(verificarGanador(simbolo,tablero)==1):
                imprimirTablero(tablero)
                break
            simbolo="o"
            jugador="La Maquina"
        else:
            movMaquina(simbolo,tablero,turno)
            if(verificarGanador(simbolo,tablero)==1):
                imprimirTablero(tablero)
                break
            jugador="El Jugador"
            simbolo="x"
        turno+=1;

    if(turno==10):
        print("-----Empate------")
        imprimirTablero(tablero)
    else:
        print(jugador+" ah ganado!")


def empezarJuegoMVSM():
    jugador="La Maquina 1"
    simbolo="x"
    
    tablero=definirTablero()
    turno=1
    while(turno<=9):
        imprimirTablero(tablero)
        print("Turno de "+jugador)
        if(simbolo=="x"):
           movMaquina(simbolo,tablero,turno)
           if(verificarGanador(simbolo,tablero)==1):
                imprimirTablero(tablero)
                break
           simbolo="o"
           jugador="La Maquina 2"
        else:
            movMaquina(simbolo,tablero,turno)
            if(verificarGanador(simbolo,tablero)==1):
                imprimirTablero(tablero)
                break
            jugador="La Maquina 1"
            simbolo="x"
        turno+=1;

    if(turno==10):
        print("-----Empate------")
        imprimirTablero(tablero)
    else:
        print(jugador+" ah ganado!")

def espacioValido(tablero,x,y):
    if(tablero[x][y]==" "):
        return 1
    else:
        return 0
  
def agregar(sim,tablero):
    while(1):
        i=int(input("Elije la fila:\n"))-1
        j=int(input("Elije la columna :\n"))-1
        if(espacioValido(tablero,i,j)):
            tablero[i][j]=sim
            return "agregado"
        else:
            print("La posicion elegida ya se encuentra en uso")
        
def verificarGanador(sim,tablero):
    i=0
    j=0
    #verificarHorizontal
    while(i<3):
        count=0
        while(j<3):
            if(tablero[i][j]==sim):
                count+=1
            j+=1
        if(count==3):
            return 1
        i+=1
        j=0
    #verificarVertical    
    i=0
    j=0
    while(i<3):
        count=0
        while(j<3):
            if(tablero[j][i]==sim):
                count+=1
            j+=1
        if(count==3):
            return 1
        i+=1
        j=0

    #verificaDiagonal
    i=0
    count=0
    while(i<3):
        if(tablero[i][i]==sim):
            count+=1
        i+=1
    if(count==3):
            return 1

    #verificaDiagonalInv
    i=0
    j=2
    count=0
    while(j>=0):
        if(tablero[i][j]==sim):
            count+=1
        j-=1
        i+=1
    if(count==3):
        return 1
        
    return 0




def movMaquina(maquina,tablero,turno):
    jugador=""
    if(maquina=="x"):
        jugador="o"
    else:
        jugador="x"
    if(turno==1 or turno==2):
        while(1):
            posInicial=[0,2];
            i=posInicial[random.randint(0,1)];
            j=posInicial[random.randint(0,1)];
            if(espacioValido(tablero,i,j)):
                tablero[i][j]=maquina
                break
        
    else:
      minmaxPodaAlfaBeta(tablero,turno,maquina)

def posicionesDisponibles(tablero):
    i=0
    posiciones=[]
    while(i<3):
        j=0
        while(j<3):
            if(tablero[i][j]==" "):
                posiciones.append(str(i)+str(j))
            j+=1
        i+=1
        
    return posiciones
            
def minmax(tablero,turno,sim):
    utilABuscar=1
    utilNoBuscar=-1
    if(sim=="x"):
       jugador="max"
    else:
        jugador="min"
        utilABuscar=-1
        utilNoBuscar=1

    if(verificarGanador(sim,tablero)):
        if(jugador=="max"):
            return 1
        else:
            return -1
    
    elif(turno==9):
        return 0
    posicionesDisp=posicionesDisponibles(tablero)
    utilidades=[]
    indices=[]
    indice=0
    

    for posAct in posicionesDisp:
        
        tableroCopia=tablero.copy()
        tableroCopia[int(posAct[0])][int(posAct[1])]=sim
        simAux="x"
        if(sim=="x"):
            simAux="o"
        turnoAux=turno+1
        utilidades.append(minmax(tableroCopia,turnoAux,simAux))
        indices.append(indice)
        indice+=1
    
    if (utilABuscar in utilidades):
        print("Util found")
        index=utilidades.index(utilABuscar);
        indice=indices[index];
        i=int(posicionesDisp[indice][0])
        j=int(posicionesDisp[indice][1])
        tablero[i][j]=sim
        return utilABuscar

    elif (0 in utilidades):
        print("0 found")
        index=utilidades.index(0);
        indice=indices[index];
        i=int(posicionesDisp[indice][0])
        j=int(posicionesDisp[indice][1])
        tablero[i][j]=sim
        return 0
    
    elif (utilNoBuscar in utilidades):
        print("No util found")
        index=utilidades.index(utilNoBuscar);
        indice=indices[index];
        i=int(posicionesDisp[indice][0])
        j=int(posicionesDisp[indice][1])
        tablero[i][j]=sim
        return utilNoBuscar
        
    else:
        print("not found")
        
    
def minmaxPodaAlfaBeta(tablero,turno,sim):
    utilABuscar=1
    utilNoBuscar=-1
    if(sim=="x"):
       jugador="max"
    else:
        jugador="min"
        utilABuscar=-1
        utilNoBuscar=1

    if(verificarGanador(sim,tablero)):
        if(jugador=="max"):
            return 1
        else:
            return -1
    
    elif(turno==9):
        return 0
    posicionesDisp=posicionesDisponibles(tablero)
    alfa=-2
    beta=2
    i=-1;
    j=-1;
    for posAct in posicionesDisp:
        
        tableroCopia=tablero.copy()
        tableroCopia[int(posAct[0])][int(posAct[1])]=sim
        simAux="x"
        if(sim=="x"):
            simAux="o"
        turnoAux=turno+1
        utilidad=minmaxPodaAlfaBeta(tableroCopia,turnoAux,simAux)
        if(jugador=="max"):
                if(alfa<utilidad):
                    alfa=utilidad
                    i=int(posAct[0])
                    j=int(posAct[1])
                    if(alfa==utilABuscar):
                        tablero[i][j]=sim
                        return alfa
        elif(jugador=="min"):
                if(beta>utilidad):
                    i=int(posAct[0])
                    j=int(posAct[1])
                    beta=utilidad
                    if(beta==utilABuscar):
                        tablero[i][j]=sim
                        return beta

    if(jugador=="max"):
        tablero[i][j]=sim
        return alfa
    elif(jugador=="min"):
        tablero[i][j]=sim
        return beta
       
    
    

empezarJuegoMVSM();

