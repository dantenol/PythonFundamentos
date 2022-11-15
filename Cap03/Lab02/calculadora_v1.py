# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("Qual operação você deseja realizar?")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite a opção desejada (1/2/3/4): "))

if (opcao < 1 or opcao > 4):
    print("Opção inválida!")
    quit()

num1 = int(input('Digite o primeiro número: '))

num2 = int(input('Digite o segundo número: '))

sum = lambda num1, num2: num1 + num2
sub = lambda num1, num2: num1 - num2
mult = lambda num1, num2: num1 * num2
div = lambda num1, num2: num1 / num2
resultado = 0
if opcao == 1:
   resultado = sum(num1, num2)
elif opcao == 2:
    resultado = sub(num1, num2)
elif opcao == 3:  
    resultado = mult(num1, num2)
elif opcao == 4:
    resultado = div(num1, num2)
else:
    print('Opção inválida!')
    quit()
print('Resultado: %s' % resultado)
