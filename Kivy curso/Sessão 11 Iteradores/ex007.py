num1 = int(input("Digite o primeiro número do intervalo: "))
num2 = int(input('Digite o segundo número do intervalo: '))
teste = 1

while num1 <= num2:
    for c in range(1, num1 +1):
        if num1%c != 0:
            continue
        elif num1%c == 0 and num1 != c and c != 1:
            break
        elif num1%c == 0 and num1 == c:
            print(num1)
    num1 += 1
