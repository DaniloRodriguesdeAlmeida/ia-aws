tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    try:
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))

        resultado = num1 / num2
        print("resultado da divisão", resultado)
        break #sai do loop se der certo
    except ValueError:
        tentativas += 1
        print(f"Erro: digite apenas números. Tentativa {tentativas}/3\n")

    except ZeroDivisionError:
        tentativas += 1
        print(f"Erro: não é impossivel dividir por zero. Tentativa {tentativas}/3\n")

    finally:
        if tentativas == max_tentativas:
            print("número máximo de tentativas atigindo. Encerrando O programa")