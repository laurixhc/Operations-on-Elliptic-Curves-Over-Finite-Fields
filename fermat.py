#Laura Henrí­quez Cazorla
#Entrega evaluable 5

#Esta función se encarga de devolver un conjunto con los puntos que pertenecen a la curva sin repetirse ninguno (p primo)
def puntos(p):
    #p primo diferente de 3
    if (p==3):
        print('p no puede ser 3')
        return
    #creamos el conjunto resultado
    resultado=set()
    #esta lista nos ayudará a tomar elementos no repetidos
    lista=[]
    inv_x=1
    #recorremos los posibles valores de x
    for x in range(0,p):
        #en el caso de ser x diferente de cero tomamos el inverso de x
        if x!=0:
            inv_x=pow(x,-1,p)
        #recorremos los posibles valores de y
        for y in range(0,p):
            #tomamos el valor de z
            z=((x**3)+(y**3))%p
            #vemos que el elemento no esté en la lista y que sea diferente del 0,0,0
            if ((z==0 and (x,y)!=(0,0)))and (((inv_x*x)%p,(inv_x*y)%p,(inv_x*z)%p) not in lista):
                lista.append(((inv_x*x)%p,(inv_x*y)%p,(inv_x*z)%p))
                resultado.add((x,y,z))
            elif z==1:
                resultado.add((x,y,z))
    return resultado
                
#Para esta función sigo las fórmulas deducidas en la parte teórica
def asterisco(P,Q,p):
    a0, a1, a2 = P
    b0, b1, b2 = Q
    if (a0**3 + a1**3 - a2**3) % p != 0 or (b0**3 + b1**3 - b2**3) % p != 0:
        print('Al menos uno de los puntos no pertenece a la curva')
        return
    
    a=(a1*b2-a2*b1)%p
    b=(a2*b0-a0*b2)%p
    c=(a0*b1-a1*b0)%p

    if a==0 and P!=Q:
        if a1==0 and b1==0: 
            inv_a0=pow(a0,-1,p)
            inv_b0=pow(b0,-1,p)
            inv_a2=pow(a2,-1,p)
            inv_b2=pow(b2,-1,p)
            c0=(inv_a0*inv_b0)%p
            c1=0
            c2=(inv_a2*inv_b2)%p
        elif a2==0 and b2==0: 
            inv_a0=pow(a0,-1,p)
            inv_b0=pow(b0,-1,p)
            inv_b1=pow(b1,-1,p)
            inv_a1=pow(a1,-1,p)
            c0=(-inv_a0*inv_b0)%p
            c1=(inv_a1*inv_b1)%p
            c2=0
        elif a0!=0 and a1!=0 and a2!=0 and b0!=0 and b1!=0 and b2!=0:
            inv_a0=pow(a0,-1,p)
            inv_b0=pow(b0,-1,p)
            inv_a2=pow(a2,-1,p)
            inv_b2=pow(b2,-1,p)
            c2=(inv_a2*inv_b2)%p
            inv=pow(a2*b0-a0*b2,-1,p)
            c0=(inv_a0*inv_b0+(a0*b1-a1*b0)*inv_a0*inv_b0*inv)%p
            c1=((a1*b0-a0*b1)*inv*c2)%p
        elif a1!=0 and a2!=0 and b1!=0 and b2!=0 and (a0==0 or b0==0):
            if a0==0:
                inv_a1=pow(a1,-1,p)
                c0,c1,c2=(0,1,a2*inv_a1)
            elif b0==0:
                inv_b1=pow(b1,-1,p)
                c0,c1,c2=(0,1,b2*inv_b1)
           
    elif a!=0 and P!=Q:
        a=-a%p
        if (b1==0 and a1!=0) or (b2==0 and a2!=0):
            a0,a1,a2=Q
            b0,b1,b2=P
        if a1!=0 and a2!=0 and b1!=0 and b2!=0:
            inv_a=pow(a,-1,p)
            inv_a1=pow(a1,-1,p)
            inv_b1=pow(b1,-1,p)
            inv_a2=pow(a2,-1,p)
            inv_b2=pow(b2,-1,p)
            c2=(((b**3)*(inv_a2*inv_b2*(inv_a**3)))+(inv_a2*inv_b2))%p
            c1=((-(c**3)*inv_a1*inv_b1*(inv_a**3))+inv_a1*inv_b1)%p
            c0=((b*c1+c*c2)*inv_a)%p
        elif a2==0:
            if b1==0: 
                inv_a=pow(a,-1,p)
                c2=(3*c*(b**2)*(inv_a)**3)%p
                c1=(-3*b*(c**2)*(inv_a)**3)%p
                c0=((b*c1+c*c2)*inv_a)%p
            else:
                inv_a=pow(a,-1,p)
                inv_b1=pow(b1,-1,p)
                inv_b2=pow(b2,-1,p)
                c2=(3*c*(b**2)*(inv_b2)*((inv_a)**3))%p
                c1=(((c**3)*inv_b1*(inv_a)**3)-inv_b1)%p
                c0=((b*c1+c*c2)*inv_a)%p
        elif a1==0:
            if b2==0: 
                inv_a=pow(a,-1,p)
                c2=(3*c*(b**2)*(inv_a)**3)%p
                c1=(-3*b*(c**2)*(inv_a)**3)%p
                c0=((b*c1+c*c2)*inv_a)%p
            elif b2!=0:
                inv_b1=pow(b1,-1,p)
                inv_b2=pow(b2,-1,p)
                inv_a=pow(a,-1,p)
                c2=(((b**3)*inv_b2*(inv_a)**3)+inv_b2)%p
                c1=(3*b*(c**2)*inv_b1*(inv_a)**3)%p
                c0=((b*c1+c*c2)*inv_a)%p
        
    elif P==Q:
        if a2==0: 
            inv_a0=pow(a0,-1,p)
            c0,c1,c2=((-((a1**2)*(inv_a0**2)))%p,1,0)
        else:
            if a1==0: 
                inv_a2=pow(a2,-1,p)
                c2=((a0**2)*(inv_a2)**2)%p
                c0,c1=(1,0)
            elif a0==0:
                inv_a2=pow(a2,-1,p)
                c2=((a1**2)*(inv_a2)**2)%p
                c0,c1=(0,1)
            else:
                inv_a0=pow(a0,-1,p)
                inv_a1=pow(a1,-1,p)
                inv_a2=pow(a2,-1,p)
                c0=(-((inv_a0)**2)+((a1**6)*(inv_a0**2)*(inv_a2**6)))%p
                c1=(((inv_a1)**2)-(a0**6)*(inv_a1**2)*(inv_a2**6))%p
                c2=(((c0*(a0**2))+(c1*(a1**2)))*(inv_a2)**2)%p
    if (c0**3 + c1**3 - c2**3) % p != 0 :
        print('Error')
        return
    if c2!=1 and c2!=0:
        inv_z=pow(c2,-1,p)
        c0,c1,c2 =((inv_z*c0)%p,(inv_z*c1)%p,(inv_z*c2)%p)
    elif c2==0 and (c0,c1,c2)!=(0,0,0):
        inv_x=pow(c0,-1,p)
        c0,c1,c2 =((inv_x*c0)%p,(inv_x*c1)%p,(inv_x*c2)%p)
    return (c0,c1,c2)

#función para sacar el inverso
def inverso(P,p):
    return asterisco((1,0,1),P,p)

#función para sacar la suma de dos puntos
def suma(P, Q, p):
    ast=asterisco(P,Q,p)
    x1,y1,z1=asterisco(ast,(1,0,1),p)
    return (x1,y1,z1)
            
#función para sacar la multiplicavión de un punto k veces
def mult(P, k, p):
    # Exponenciación binaria para calcular kP

    result = (1, 0, 1)  # Punto en el infinito
    base = P

    while k > 0:
        # Si el bit menos significativo de k es 1, multiplicar por la base actual
        if k % 2 == 1:
            result = suma( base,result, p)
        # Duplicar la base actual
        base = suma(base, base, p)

        # Desplazar a la derecha los bits de k
        k //= 2

    return result
