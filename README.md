# Calculadora.py
 calculadora simples em python 

Passo 1: Início do programa
O programa começa com uma variável op definida como uma string vazia (''), que será usada para armazenar a escolha do usuário sobre qual operação matemática deseja realizar.
op = ''

Passo 2: Laço de repetição
O programa entra em um laço while que só será interrompido quando o usuário digitar 's' para sair.
while op != 's':

Passo 3: Exibir menu de operações
Dentro do laço, o programa exibe um menu com as opções de operações matemáticas (soma, subtração, multiplicação, divisão) e a opção de sair (digitando 's').
op = input('''Qual a operação desejada? Escolha dentre as seguintes opções:
'+' para soma
'-' para subtração
'*' para multiplicação
'/' para divisão
's' para sair do programa
operação = ''')
Aqui, o programa aguarda a entrada do usuário para escolher uma das opções.

Passo 4: Verificar se o usuário deseja sair
Se o usuário digitar 's', o programa irá sair do laço de repetição e, consequentemente, terminará a execução. Caso contrário, o programa continuará pedindo os números para realizar a operação escolhida.
if op == 's':
    break

Passo 5: Capturar os números inseridos pelo usuário
O programa solicita ao usuário que insira dois números inteiros (para realizar a operação escolhida). Esses números são armazenados nas variáveis n1 e n2.
try:
    n1 = int(input('1° número: '))
    n2 = int(input('2° número: '))
except ValueError:
    print('Por favor, entre com números inteiros!')
    continue  # Caso ocorra um erro, pede os números novamente
Tratamento de erro: Se o usuário digitar algo que não seja um número inteiro (por exemplo, um valor como "abc"), o programa exibirá uma mensagem de erro e continuará pedindo os números. Isso é feito através de um try-except que captura o erro ValueError.

Passo 6: Realizar a operação
O programa verifica qual operação foi escolhida (armazenada na variável op) e, com base nisso, realiza a operação correspondente:

Soma ('+'): Se o usuário escolheu a soma, o programa executa a soma entre n1 e n2 e exibe o resultado.
if op == '+':
    print(f'{n1} + {n2} = {n1 + n2}')
Subtração ('-'): Se o usuário escolheu a subtração, o programa executa a subtração entre n1 e n2 e exibe o resultado.
elif op == '-':
    print(f'{n1} - {n2} = {n1 - n2}')
Multiplicação ('*'): Se o usuário escolheu a multiplicação, o programa executa a multiplicação entre n1 e n2 e exibe o resultado.
elif op == '*':
    print(f'{n1} * {n2} = {n1 * n2}')
Divisão ('/'): Se o usuário escolheu a divisão, o programa verifica se o divisor (n2) é zero, pois a divisão por zero não é permitida. Se n2 for diferente de zero, o programa realiza a divisão e exibe o resultado. Caso contrário, exibe uma mensagem de erro.
elif op == '/':
    try:
        print(f'{n1} / {n2} = {n1 / n2}')
    except ZeroDivisionError:
        print('Divisão por zero não permitida!')
    print('-----------------------------------')
Tratamento de erro de divisão por zero: Se n2 for igual a zero, o programa irá capturar o erro ZeroDivisionError e exibirá uma mensagem de erro.

Passo 7: Voltar ao menu
Após a execução de uma operação, o programa exibirá uma linha de separação (-----------------------------------) e voltará ao menu principal, pedindo uma nova operação ou a opção de sair.

Passo 8: Finalização do programa
O laço continuará até que o usuário digite 's'. Quando isso acontecer, o programa imprime a mensagem "Programa finalizado!" e termina a execução.
print('Programa finalizado!')


Espero que este passo a passo tenha ficado claro e ajude você a entender como o programa funciona!

