"""En la llamada al botón Button, debes pasar la función reset sin ejecutarla. 
Por lo tanto, debes quitar los paréntesis en command=reset()"""
import copy
from tkinter import *
import tkinter as tk
from tkinter import ttk

def get_generation(cells,y):
    y=int(y)
    L = cells
    M = copy.deepcopy(L)
    for n3 in range(y):
        L = copy.deepcopy(M)
        M = copy.deepcopy(L)
        u = 0
        h=0
        r=0
        h2 =0
        for j, n in enumerate(L):
            for i, n2 in enumerate(L[j]):
                
                P = 0
                if j==0 and i==0: #ezquina superior izquierda
                    P += sum(L[j][i:i+2])+sum(L[j+1][i:i+2])#0000000000000
                elif j==0 and i==len(L[j])-1:#lo que mide la fila j en la matriz l, hasta el final, tiene que ser -1 por que len cuenta los elemntos
                #que es este caso son 2, pero enumarate como que los va contanto 1 a 1 pero desde 0 entonces es 1 menos 
                    P += sum(L[j][i-1:i+1])+sum(L[j+1][i-1:i+1])
                elif j==len(L)-1 and i == 0: #ezquina inferior izquierda
                    P +=sum(L[j-1][i:i+2])+sum(L[j][i:i+2])
                elif j== len(L)-1 and i== len(L[j])-1:#ezquina inferior derecha
                    P += sum(L[j][i-1:i+1])+sum(L[j-1][i-1:i+1])

        
                elif j==0:#borde superior
                    P += sum(L[j][i-1:i+2])+sum(L[j+1][i-1:i+2])
                
                elif i==0:#borde izquierdo
                    P = sum(L[j-1][i:i+2]) + sum(L[j][i:i+2])+sum(L[j+1][i:i+2])
            
                elif i ==len(L[j])-1:#borde derecho
                    P = sum(L[j-1][i-1:i+1]) + sum(L[j][i-1:i+1])+sum(L[j+1][i-1:i+1])
            
                elif j == len(L)-1:#borde inferior
                    P += sum(L[j][i-1:i+2])+sum(L[j-1][i-1:i+2])
            
                else:
                    P = sum(L[j-1][i-1:i+2]) + sum(L[j][i-1:i+2])+sum(L[j+1][i-1:i+2])
                
                P -= L[j][i]
                if P < 2 or P > 3:
                    M[j][i] = 0
                elif P == 3:
                    M[j][i] = 1
        for j, n in enumerate(L):
            for i, n2 in enumerate(L[j]):
                #if j==0 solo se me ocurre hacer una variable para ver si ya pase por aqui como un contador 
                    
                if j==0 and not i==0 and not i ==len(L[j])-1:#---------------borde supeior     
                    if u != 0 and sum(L[j][i-1:i+2]) == 3:
                        M[0][i]=1 
                    elif sum(L[j][i-1:i+2]) == 3:       #60
                        M.insert(0,[0]*(len(M[0])))
                        M[0][i]=1 
                        u += 1 #al parecer si es necesario
                    
                elif i==0 and not j==0 and not j == len(L)-1:#----------------------borde izquierdo
                    if h ==1 and L[j][i] + L[j+1][i] + L[j-1][i] ==3:
                        M[j+u][i] = 1
                    elif L[j][i] + L[j+1][i] + L[j-1][i] ==3:
                        M = [[0] + fila for fila in M]
                        M[j+u][i] = 1 #la variable de las pruebas parece que no es necesaria talvez 
                        h=1
                        
                elif i ==len(L[j])-1 and not j==0 and not j == len(L)-1:#borde derecha
                    if h2 ==1 and L[j][i] + L[j+1][i] + L[j-1][i] ==3:
                        M[j+u][i+1+h2] = 1
                    elif L[j][i] + L[j+1][i] + L[j-1][i] ==3:
                        M= [fila + [0] for fila in M]
                        M[j+u][i+1+h+h2] = 1 #raro qeu sea 2 pero asi funciona de maravilla en la 16 generacion
                        h2=1
                        continue

                elif j == len(L)-1 and not i==0 and not i ==len(L[j])-1:#borde inferior
                    if sum(L[j][i-1:i+2]) == 3 and r == 1 :#error
                        M[j+1+u][i]=1
                    elif sum(L[j][i-1:i+2]) == 3:
                        r =1
                        M.append([0]*len(M[0]))
                        M[j+1+u][i]=1
                        continue
        for q,p in enumerate(M): # esto se agrega por su hay una fila vacia se elimine
            if sum(p) == 0 and (q == 0 or q ==(len(M)-1)):
                M.pop(q)
            
        z=0
        z1=0
        #l.pop() #saca el ultimo elemento de la lista 
        try:
            
            for n,f in enumerate(M):
                z+=f[0]
                z1+=f[-1]
            if z1 ==0:
                [fila.pop() for fila in M]
            if z == 0:
                [fila.pop(0) for fila in M]
        except IndexError: 
            M = [[0,0],[0,0]]
            Y=n3
            return M
        if len(M) < 2:
            M.append([0]*len(M[0]))
        
        U=0#esto es por que cabe la posibilidad de que se genere una lista asi [[],[]] osea vacia y si esta vacia pues que pase a esto [[0],[0]]
        #para que el canvas la dibuje
        for o in M:
            U+=len(o)
        if U== 0:
            M =[[0,0],[0,0]]        
        I=0 #esto es para cuando alla una linea de unos en diferentes filas y no tengas mas elementos darles un elemntos mas de ceros para que tenga 
        #donde generar la siquiente generacion sin problema
        #pasa de algo asi [[1],[1],[1]] q [[0,1],[0,1],[0,1]] por lo que es una linea muy delgada el programa no reconoce el espacio para generar mas 
        for fila in M:
            I += len(fila)
        if I == len(M):
            M = [[0] + fila for fila in M]
    return M 

#-----------------------------------------------------------------------------------

def visual(T):
    def mostrar_matriz(T):
        for i, fila in enumerate(T):
            label = Label(marco5,text = i+1)
            label.pack()
            label.config(font=('time new roman',12))
            for j, valor in enumerate(fila):
                color = "red" if valor == 1 else "blue"
                canvas.create_rectangle(
                    j * TAMANO_CELDA,
                    i * TAMANO_CELDA,
                    (j + 1) * TAMANO_CELDA,
                    (i + 1) * TAMANO_CELDA,
                    fill=color
                        )
    # Tamaño de cada celda en píxel
    TAMANO_CELDA = 24
    b=0
    def reset():
        b=1
        root.destroy()
        JD(G, generacion.get())

    # Crear la ventana principal
    root = tk.Tk()
    root.config()

    root.title("Juego de la Vida de Conway")
    
    marco1 = Frame(root)#marco global
    marco1.pack()
    
    marco2 = Frame(marco1)#marco de arriba
    marco2.pack(side='top')
    
    marco3 = Frame(marco2) #marco de arriba del de arriba 
    marco3.pack(side='top')

    marco4 = Frame(marco2)#marco central que van 3 elementos 
    marco4.pack(side='bottom')
    
    marco10 = Frame(marco1)
    marco10.pack()#mcambiar a nada si no funciona 

    marco5 = Frame(marco10)
    marco5.pack(side='left')#mcambiar a nada si no funciona 

    marco6 = Frame(marco10)
    marco6.pack()#marco del canvas

    marco7 = Frame(marco1)
    marco7.pack(side='bottom')#marco del numeros de abajo

    labelnumrtodegeneracion = Label(marco3, text = f"Generacion  # {y2}" if b==0 else f'Gneracion:{generacion.get()}')  #cuando inicia el programa con un texto
    #y cuando se itera con otro 
    labelnumrtodegeneracion.pack()

    generacion = StringVar()  
    
    label4 = Label(marco4, text ='Numero de la nueva generacion')
    label4.pack(side='left')

    entry = Entry(marco4, textvariable=generacion ,width=5)#widh es para que lo largo que cera el largo de texto
    entry.pack(side='left')
    
    B=Button(marco4, text='Crear', command=reset)
    B.pack(side ='right')

   
    

    #Button(root, text='Generacion', command=reset).pack()

    # Crear un lienzo (canvas)
    canvas = tk.Canvas(marco6, width=len(T[0]) * TAMANO_CELDA, height=len(T) * TAMANO_CELDA)
    canvas.pack(side='left')

    l = ' '.join('  ' + str(x) for x in list(range(1, len(T[1])+1)))
    if len(T) > 5:
        l = '   ' + l

    label8 = Label(marco7, text='   ')
    label8.pack(side='left')
    
    label3 = Label(marco7, text=l)
    label3.pack(side='left')
    label3.config(font=('time nue roman',11),padx=100)
    # Mostrar la matriz en el lienzo
    if  T == [[0,0],[0,0]]:
        labelmuerta = Label(root,text= f'NO HAY VIDA EN LA GENERACION #{y2} CON LAS CONDICIONES INICIALES ACTUALES'  )
        labelmuerta.pack()
    mostrar_matriz(T)

    root.mainloop()

def JD(M3, y):
    global G #DEFINIR VARIABLE GLOBAL PARA QUE SEA ACCECIBLE DESDE CUALQUIER LADO 
    global y2
    y2= y
    G = M3
    T = get_generation(M3, y)
    visual(T)

# Definir M3 aquí o donde corresponda en tu aplicación.

JD([[0,0,0,0,0,0],[0,1,1,0,1,0],[0,1,1,0,1,0],[0,1,1,0,1,0],
    [0,0,0,0,0,0]], 6)
'''
# Variable global
variable_global = 10

def modificar_variable_global():
    # Indicar que se está utilizando la variable global
    global variable_global
    # Modificar el valor de la variable global
    variable_global = 20

# Antes de llamar a la función
print("Antes de la función:", variable_global)

# Llamada a la función que modifica la variable global
modificar_variable_global()

# Después de llamar a la función
print("Después de la función:", variable_global)'''