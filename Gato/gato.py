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

def verificarProximoAganar(sim,contrincante,tablero):
    i=0
    j=0
    aux=0
    print("verificarHorizontal")
    while(i<3):
        count=0
        while(j<3):
            if(tablero[i][j]==sim ):
                count+=1
            elif(tablero[i][j]==" "):
                aux=j
            j+=1
        if(count==2 and espacioValido(tablero,i,aux)):
            return str(i)+str(aux)
        i+=1
        j=0
    print("verificarVertical")    
    i=0
    j=0
    aux=0
    while(i<3):
        count=0
        while(j<3):
            if(tablero[j][i]==sim ):
                count+=1
            elif(tablero[j][i]==" "):
                aux=j
            j+=1
        if(count==2 and espacioValido(tablero,aux,i)):
            return str(aux)+str(i)
        i+=1
        j=0
        
    print("verificaDiagonal")
    i=0
    count=0
    aux=0
    while(i<3):
        if(tablero[i][i]==sim ):
            count+=1
        elif(tablero[i][i]==" "):
            aux=i
        i+=1
    if(count==2 and espacioValido(tablero,aux,aux)):
            return str(aux)+str(aux)

    print("verificaDiagonalInv")
    i=0
    j=2
    count=0
    aux=0
    aux2=0
    while(j>=0):
        if(tablero[i][j]==sim):
            count+=1
        elif(tablero[i][j]==" "):
            aux=i
            aux2=j
        i+=1
        j-=1
    if(count==2 and espacioValido(tablero,aux,aux2) ):
            return str(aux)+str(aux2)
        
    return "null"

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
        pos1=verificarProximoAganar(maquina,jugador,tablero)
        if(pos1=="null"):
            pos=verificarProximoAganar(jugador,maquina,tablero)
            if(pos!="null"):
                print(pos)
                tablero[int(pos[0])][int(pos[1])]=maquina
            else:
                while(1):
                    posInicial=[0,2];
                    i=posInicial[random.randint(0,1)];
                    j=posInicial[random.randint(0,1)];
                    if(espacioValido(tablero,i,j)):
                        tablero[i][j]=maquina
                        break
        else:
            print(pos1)
            tablero[int(pos1[0])][int(pos1[1])]=maquina
         
        
    
    

empezarJuegoM();

