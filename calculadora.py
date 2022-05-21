import re # pacote com as rotinas de expressão regular

#Função criada para checkar se foi realmente informado um número inteiro ou uma string.
def check_number(number):
    pattern_int = re.compile(r"(0|-?[1-9][0-9]*)")
    while True:
        if pattern_int.match(number):
            number = int(number)
            return number
        else:
            print("Por favor informe um número!")
            number = input("Número a ser informado: ")

#Textos exibidos na aplicação
menu_opcao_text = """----- Calculadora -----
Selecione uma Opção:
Opção 1 - Adição
Opção 2 - Subtração
Opção 3 - Multiplicação
Opção 4 - Divisão
----- Calculadora -----
Opção: """

submenu_opcao_text = """Deseja continuar usando a calculadora?
1 - Sim.
2 - Não.
"""

## Funções de contas

#Adição
def adicao(x, y):
    resultado = x + y
    return resultado

#Subtração
def subtracao(x, y):
    resultado = x - y
    return resultado

#Multiplicação
def multiplicacao(x, y):
    resultado = x * y
    return resultado

#Divisão
def divisao(x, y):
    resultado = x / y
    return resultado

## Menu da calculadora realizando chamada das funções de cálculo
def menu():
    opcao = input(menu_opcao_text)
    while opcao not in ('1','2','3','4'):
        print("Selecione a opção correta!")
        opcao = input(menu_opcao_text)
    x = input("Informe o primeiro número: ")
    x = check_number(x)
    y = input("Informe o segundo número: ")
    y = check_number(y)
    if opcao == '1':
        resultado = adicao(x,y)
    elif opcao == '2':
        resultado = subtracao(x,y)
    elif opcao == '3':
        resultado = multiplicacao(x,y)
    elif opcao == '4':
        resultado = divisao(x,y)
    print(resultado)
     
# Execução da aplicação enquanto é solicitado continuar na cálculadora
while True:
    menu()
    continuar = input(submenu_opcao_text)
    while continuar not in ('1','2'):
        print("Selecione a opção correta!")
        continuar = input(submenu_opcao_text)
    if continuar == '2':
        break
