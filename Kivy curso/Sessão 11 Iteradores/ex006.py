num = 1

while num <= 100:
    for c in range(1, num +1):
        if num%c != 0:
            continue
        elif num%c == 0 and num != c and c != 1:
            break
        elif num%c == 0 and num == c:
            print(num)
    num += 1