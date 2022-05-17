#Se asume que el primer valor ingresado por el usuario en el arreglo es el valor META
#Se asume que la combinacion de numeros es de solo 2 digitos
#Se asumira que la combinacion correcta en caso de empate es la que tenga el numero mayor.

def mostrarFormulario():
 Post = [11,2,3,4,5,6,7]
 return Post

def mejorCalce():
    
    arreglo = mostrarFormulario()
    aux_arreglo = arreglo
    comprobar = bool

    for i in range(1,len(arreglo)):

        if arreglo[0] == arreglo[i]:

            print('Felicidades encontro un calce el cual es: ' + str(arreglo[i]) + ' a su valor meta: ' + str(arreglo[0]) + ' "sin combinacion"')
            comprobar = False
            break
        
        else:
            comprobar = True
            
    if  comprobar:     
        suma_temporal = 0
        ultima_suma = 0
        mejor_suma = 0
        mejor_combi = 0

        for x in arreglo:
                    
            aux_arreglo = aux_arreglo[1:] 
                    
            for y in aux_arreglo:
                    
                ultima_suma = int(x) + int(y)
                        
                if ultima_suma <= arreglo[0] and ultima_suma > suma_temporal:
                    suma_temporal = ultima_suma
                    mejor_combi = str(x) + "," + str(y)
                            

        if suma_temporal > mejor_suma:
            mejor_suma = suma_temporal
            print("Calce para meta: " + str(arreglo[0]) + " es la suma de: " + str(mejor_suma) + " con la combinacion: " + str(mejor_combi))
                    
                
print(mostrarFormulario())

preguntar = True

while preguntar: 

    for recorrer in mostrarFormulario():

        if recorrer > 0 and recorrer % 1 == 0:
            print("El numero ingresado es entero y positvo")
            
        else:
            print("El numero ingresado no es entero o no es positivo")
            print("Ingresa nuevamente los datos en el formulario")
            mostrarFormulario()
            preguntar = False

    print("Todo el contenido fue validado se puede seguir con la siguiente etapa")
    mejorCalce()
    preguntar = False