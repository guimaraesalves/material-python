
while True:
    try:
        valor = input().split(" ")
        num1, num2 = valor
        print(int(num1)^int(num2))
    except (EOFError):
        break 
                 
