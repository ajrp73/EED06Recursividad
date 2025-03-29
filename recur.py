#Escriba una función recursiva que reciba una lista con sublistas de números enteros y obtenga su suma
def sumaListaSubListasEnteros(lista):
    if len(lista) == 0:
        return 0
    else:
        return sum(lista[0]) + sumaListaSubListasEnteros(lista[1:])
print("suma lista: ", sumaListaSubListasEnteros([[0, 1, 2], [3,4,5], [6,7,8], [9]]))

#Escriba una función recursiva que reciba una cadena de carácteres y devuelva la cadena en orden inverso
def cadenaInversa(cad, caracRestantes):
    if caracRestantes==0:
        return ""
    else:
        return cad[-1]+cadenaInversa(cad[:-1], caracRestantes-1)
    
print ("hola:",cadenaInversa("hola", 4))


#Escriba una función recursiva que reciba un carácter y un entero y devuelva una cadena formada por el caracter repetido
#tantas veces como indique el entero
def multCaracter(c, nveces):
    if nveces == 0:
        return ""
    return "" + c + multCaracter(c, nveces-1)

print ("5 veces ?: ",multCaracter('?', 5))


#Escriba una función recursiva que devuelva una cadena con los n términos de la sucesión de Fibonacci
def fiboRecur(n1, n2, t, numTerminos):
    print (f"({n1}, {n2})")
    if t == numTerminos:
        return ""
    else:
        if t==0:
            return "0 " + fiboRecur(0, 1, t+1, numTerminos)
        if t==1:
            return "1" + fiboRecur(0, 1, t+1, numTerminos)
        else:
            return " " + str(n1+n2) + fiboRecur(n2, n1+n2, t+1, numTerminos)
    
print("fibo 4 términos: ", fiboRecur(0, 1, 0, 4))