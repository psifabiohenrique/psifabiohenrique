inicio_intervalo = int(input('Digite o primeiro número do intervalo: '))
final_intervalo = int(input('Digite o segundo número do intervalo: '))
num1 = int(input('Digite o primeiro número a ser ignorado: '))
num2 = int(input('Digite o segundo número a ser ignorado: '))
num3 = int(input('Digite o terceiro número a ser ignorado: '))

while inicio_intervalo <= final_intervalo:
    if inicio_intervalo == num1 or inicio_intervalo == num2 or inicio_intervalo == num3:
        inicio_intervalo += 1
        continue
    print(inicio_intervalo)
    inicio_intervalo += 1
    