# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)