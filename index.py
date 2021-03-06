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

def verificar_produto(idade, limite):
    n = int(input('Quantidade de produtos que deseja cadastrar: '))
    total = 0
    limite_atual = limite

    for x in range(n):
        produto = input('Informe o nome do produto que deseja:')
        valor = float(input('Informe o preço deste produto: R$'))
        total += valor
        limite_atual -= valor
        print('Total: R${0:.2f}. Limite disponível: R${1:.2f}'.format(total, limite_atual))
    
    if total <= (0.6*limite_atual):
        print('Liberado!')
    elif total > (0.6*limite_atual) and total < (0.9*limite_atual):
        print('Liberado ao parcelar em até 2 vezes.')
    elif total > (0.9*limite_atual) and total < (1.0*limite_atual):
        print('Liberado ao parcelar em 3 ou mais vezes.')
    else:
        print('Bloqueado!')    
    if total > 26 and total < idade:
        desconto = total - (total*0.05)
        print('Você terá um desconto de 5%, seu produto custará R$ {:.2f}'.format(desconto))

idade, limite = obter_limite()
verificar_produto(idade, limite)
