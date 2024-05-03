letras = ["a", "b", "c", "d"] #lista con varios elementos (pueden ser de cualquier tipo)

numeros = [0, 1, 2, 3, 4, 5.6] #Lista con valores numéricos Int y Float

letras [0] #llamado del elemento específico, siempre se comienza en 0

letras [1]

letras [2]

letras [3]

letras.append ("e") #Agrega un elemento nuevo al final de la lista

letras.insert (0, "A") #Agrega un elemento nuevo en la posición deseada, dentro de l paréntesis el primar valor es la posición dentro de la lista y el segundo es el valor en sí mismo

"A" in letras #Busca sí existe el elemento indicado dentro de la lista, responde un valor booleano

letras.remove ("a") #Elimina un elemento específico de la lista

letras.index ("c") #Devuelve el numero de posición donde se encuentra ubicado el elemento deseado dentro de la lista especificada

letras [2] = "C" #Cambia el elemento indicado por el índice del corchete por otro elemento

letras.count ("d") #Cuenta cuantos elementos "d" hay dentro de la lista

numeros.reverse () #Reversa el orden de la lista "numeros"

numeros.extend ([6, 7, 8.3, 9, True, False]) #Adiciona un conjunto de valores [6, 7, 8.3, 9] al final de la lista "numeros"

letras.extend (numeros) #Adiciona la lista "numeros" dentro de la lista "letras"

letras.pop () #No tengo idea de su funcionamiento

letras.sort () #No tengo idea de su funcionamiento

print(letras)