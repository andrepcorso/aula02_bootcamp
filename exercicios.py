# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#num_01 = int(input("Digite um número inteiro: "))
#num_02 = int(input("Digite outro número inteiro: ")) 

#resultado = num_01 + num_02

#print(f"A soma dos dois números é igual a {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

#num_usuario = int(input("Digite um número inteiro: "))

#resto_divisao = num_usuario % 5

#print(f"O resto da divisão do número {num_usuario} por 5 é igual a {resto_divisao}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#num_01 = int(input("Digite um número inteiro: "))
#num_02 = int(input("Digite outro número inteiro: ")) 

#resultado = num_01 * num_02

#print(f"A multiplicação entre os dois números é igual a {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#num_01 = int(input("Digite um número inteiro: "))
#num_02 = int(input("Digite outro número inteiro: ")) 

#resultado = num_01 // num_02

#print(f"A divisão inteira entre os dois números é igual a {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#num_01 = int(input("Digite um número inteiro: "))

#resultado = num_01 ** 2

#print(f"O quadrado desse número é igual a {resultado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

#num_01 = float(input("Digite um número inteiro: "))
#num_02 = float(input("Digite outro número inteiro: ")) 

#resultado = num_01 + num_02

#print(f"A soma dos dois números é igual a {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#num_01 = float(input("Digite um número inteiro: "))
#num_02 = float(input("Digite outro número inteiro: ")) 

#resultado = (num_01 + num_02)/2

#print(f"A média dos dois números é {resultado}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

#num_01 = float(input("Digite um número base: "))
#num_02 = float(input("Digite um expoente: ")) 

#resultado = num_01 ** num_02

#print(f"{num_01} elevado a {num_02} é igual a {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#temp_celsius = float(input("Digite uma temperatura em Celsius: "))

#temp_fahrenheit = temp_celsius * 1.8 + 32

#print(f"{temp_celsius} graus Celsius equivalem a {temp_fahrenheit} graus Fahrenheit ")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#import math

#raio = float(input("Digite o raio de um círculo: "))

#area =  math.pi * raio ** 2

#print(f"A área do círculo com raio {raio} é igual a {area}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#texto = (input("Digite um texto: "))

#maisculo = texto.upper()

#print(maisculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#texto = (input("Digite um texto: "))

#minusculo = texto.lower()

#print(minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#texto = (input("Digite um texto: "))

#strip = texto.strip()

#print(strip)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

#data = (input("Digite uma data no formato dd/mm/aaaa "))

#sep = data.split("/")

#print(f"Dia {sep[0]}, Mês {sep[1]}, Ano {sep[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

#nome = input("Digite um nome: ")
#sobrenome = input("Digite um sobrenome: ")

#print(f"O nome completo é {nome} {sobrenome}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# Exemplo de entrada
#valor1 = False
#valor2 = False
#resultado_and = valor1 and valor2
#print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# Exemplo de entrada
#valor1 = False
#valor2 = True
#resultado_or = valor1 or valor2
#print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# Exemplo de entrada

#valor1 = False
#valor2 = True
#resultado_not = not valor1
#print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# Exemplo de entrada
#num1 = 5
#num2 = 4
#resultado_igualdade = (num1 == num2)
#print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# Exemplo de entrada
#num1 = 5
#num2 = 4
#resultado_diferenca = (num1 != num2)
#print("Resultado da diferença:", resultado_diferenca)

# #### try-except e if

# 21: Conversor de Temperatura

# try:
#     temp_celsius = float(input("Digite uma temperatura em Celsius: "))
#     temp_fahrenheit = temp_celsius * 1.8 + 32
#     print(f"{temp_celsius} graus Celsius equivalem a {temp_fahrenheit} graus Fahrenheit ")
# except ValueError:
#     print("Você não digitou um número")


# 22: Verificador de Palíndromo
    
# try:
#     palavra = input('Digite uma palavra: ')

#     if not palavra.isalpha() or len(palavra) < 3:
#             raise ValueError("A palavra deve conter apenas letras e ter mais de 2 caracteres")
    
#     palavra_min = palavra.lower()
#     palavra_inv = palavra_min[::-1]
    
#     if palavra_min == palavra_inv:
#         print("A palavra é um palíndromo")
#     else:    
#         print("A palavra não é um palíndromo")

#except ValueError as e:
#    print(e)

       
# 23: Calculadora Simples

# try:
#     num_01 = float(input("Digite um número: "))
#     num_02 = float(input("Digite um número: "))
#     sinal = input("Qual a operação gostaria de fazer? (Digite +, - , * ou /): ")


     
    
#     if sinal == "+":
#         resultado = num_01 + num_02
#         print(f"O resultado da adição é igual a {resultado}")
#     elif sinal == "-":
#         resultado = num_01 - num_02
#         print(f"O resultado da subtração é igual a {resultado}")
#     elif sinal == "*":
#          resultado = num_01 * num_02
#          print(f"O resultado da multiplicação é igual a {resultado}")
#     elif sinal == "/":
#          resultado = num_01/num_02
#          print(f"O resultado da divisão é igual a {resultado}")
#     else:    
#         print("Não compreendi qual operação quer fazer")
    

# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")

# except ValueError:
#     print("Erro: Entrada inválida. Por favor, insira um número válido.")


# 24: Classificador de Números

try:

    num = float(input("Digite um número: "))

    if num > 0:
        tipo = "positivo"
    elif num < 0:
        tipo = "negativo"
    else:
        tipo = "zero"

    if num % 2 == 0:
        ip = "par"
    else:
        ip = "ímpar"

    print(f"O número digitado é {tipo} e {ip}")

except ValueError:
     print("Erro: Entrada inválida. Por favor, insira um número válido.")

# 25: Conversão de Tipo com Validação
