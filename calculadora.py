op = ''
while op != 's' :
 op = input('''qual a operação desejada? escolha dentre as seguintes opções:
 '+'
 '-'
 '*'
 '/'
 's' para sair do programa

 operação = ''')

 if op == 's':
    break

 try:
       n1 = int(input('1° número:'))
       n2 = int(input('2° número:'))
 except:
        print('entrar com números inteiros!')
 else:
  if op == '+':
    print(f'{n1} + {n2} = {n1 + n2}')
  elif op == '-':
    print(f'{n1} - {n2} = {n1 - n2}')
  elif op == '*':
    print(f'{n1} * {n2} = {n1 * n2}')
  else:
    try:
         print(f'{n1} / {n2} = {n1 / n2}')
    except:
          print('divisão por zero não permitida!!!')
          print('-----------------------------------/n')

print('programa finalizado!')
