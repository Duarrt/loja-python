def obter_limite():
    print('Olá, seja bem vindo à DuarrtShop! Sou o Ramon Duarte, como posso ajudar?')
    print('Iremos fazer uma análise do seu crédito, por gentileza, responda as seguintes questões: ')
    cargo = input('Qual seu cargo atual?')
    salario = float(input('Quanto você ganha neste cargo?'))
    datanasc = input('Qual seu ano de nascimento?')
    print('Segundo os dados informados, seu cargo é {0}, ganha R${1:.2f} e nasceu no ano de {2}.'.format(cargo, salario, datanasc))
    
    idade = 2021 - int(datanasc) 
    limite = salario * (idade/1000) + 100
    print('Sua idade é de ' + str(idade) + ' anos. E você terá um limite de R${:.2f}!'.format(limite))
    return idade, limite

idade, limite = obter_limite()

def verificar_produto(idade, limite):
    produto = input('Informe o nome do produto que deseja:')
    valor = float(input('Informe o preço deste produto: R$'))
    return limite_disp(idade, limite, valor)
        

def limite_disp(idade, limite, valor):
    if valor <= (0.6*limite):
        print('Liberado!')
    elif valor > (0.6*limite) and valor < (0.9*limite):
        print('Liberado ao parcelar em até 2 vezes.')
    elif valor > (0.9*limite) and valor < (1.0*limite):
        print('Liberado ao parcelar em 3 ou mais vezes.')
    else:
        print('Bloqueado!')    
    if valor > 26 and valor < idade:
        desconto = valor - (valor*0.05)
        print('Você terá um desconto de 5%, seu produto custará R$ {:.2f}'.format(desconto))
    return limite-valor
# verificar_produto(idade, limite)

n = int(input('Quantidade de produtos que deseja cadastrar: '))
for x in range(n):
    limite = verificar_produto(idade, limite)
    
#    prod = input('Entre com o item {}: '.format(x+1))
#    valor = input('Entre com o valor do item {}'.format(x+1))
#    total = total + valor
#    limite_disponivel = limite - total
#    print("")