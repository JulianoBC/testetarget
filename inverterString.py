def inverterString(string):
    #essa é uma das formas de inverter uma string sem usar reverse, usando fatiamento, onde olhando a documentação da string podemos encontrar [inicio:fim:passo] e colocando o passo -1 ele inverte a entrada
    stringInvertida = string[::-1]
    return stringInvertida

string = input("Digite uma string: ")

stringInvertida = inverterString(string)
print(f"A string invertida é : {stringInvertida}")