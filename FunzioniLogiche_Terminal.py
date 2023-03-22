def sommaBin(lista):
    dim = len(lista)
    for i in range(dim-1, -1,-1):
        if not lista[i]:
            lista[i] = True
            for r in range(i+1, dim):
                lista[r] = False
            break
        
    return lista

print("La variabili della funzione devono essere espresse come dei singoli caratteri maiuscoli (A, B, C...)")
print("Gli operatori logici DEVONO essere espressi con le seguenti forme: ")
print("AND => * ")
print("OR => + ")
print("NOT => ! ")
print("Usare le parentesi tonde nel caso fosse necessario")
print("Inserire la funzione logica: ")
Fx = input()

indexVar = -1
carUsed = []
boolVar = []
comandoFinale = ''#stringa che conterrà la formula analizzata e codificata correttamente


for c in Fx:
    #controllo dei vari possibili  operatori logici
    if c == '*':
        comandoFinale += ('and ')
    if c == '+':
        comandoFinale += ('or ')
    if c == '!':
        comandoFinale += ('not ')

    #controllo varibili
    if ord(c) >= 65 and ord(c) <= 90:
        try:
            indice = carUsed.index(c)
        except ValueError:
            indexVar+=1
            carUsed.append(c)
            boolVar.append(False)
        indice = indexVar

        comandoFinale += ("boolVar["+str(indice)+"] ")

    #controllo se parentesi
    if c == '(':
        comandoFinale += ('( ') 
    
    if c == ')':
        comandoFinale += (' )')

carUsed.sort()
FxCalcolata = ''
strFinal = ''

for c in carUsed:
    strFinal += c
strFinal += " Fx"
print(strFinal)

for i in range(pow(2,indexVar+1)):
        if eval(comandoFinale):
            FxCalcolata = '1'
        else:
            FxCalcolata = '0'

        #output
        strFinal = ''

        for r in range(indexVar + 1):
            if boolVar[r]:
                strFinal += "1"
            else:
                strFinal += "0"
        
        strFinal += ' ' + FxCalcolata

        print(strFinal)
        #gestione tabella di verita
        boolVar = sommaBin(boolVar)
