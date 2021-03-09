def obter_limite():
    print('Olá, seja bem vindo à DuarrtShop! Sou o Ramon Duarte, como posso ajudar?')
    print('Iremos fazer uma análise do seu crédito, por gentileza, responda as seguintes questões: ')
    cargo = input('Qual seu cargo atual?')
    salario = input('Quanto você ganha neste cargo?')
    datanasc = input('Qual seu ano de nascimento?')
    print('Segundo os dados informados, seu cargo é ' + cargo + ', ganha R$' + salario + ' e nasceu no ano de ' + datanasc + '.')
    
    global idade
    idade = 2021 - int(datanasc)
    global credit 
    credit = (int(salario) * (idade/1000) + 100)
    print('Sua idade é de ' + str(idade) + ' anos. E você terá um limite de R$' + str(credit) + '!')
    global limite 

obter_limite()
limite = credit

def verificar_produto(limite):
    produto = input('Informe o nome do produto que deseja:')
    valor = input('Informe o preço deste produto: R$')
    if int(valor) <= (0.6*limite):
        print('Liberado!')
    elif int(valor) > (0.6*limite) and int(valor) < (0.9*limite):
        print('Liberado ao parcelar em até 2 vezes.')
    elif int(valor) > (0.9*limite) and int(valor) < (1.0*limite):
        print('Liberado ao parcelar em 3 ou mais vezes.')
    else:
        print('Bloqueado!')    
    if int(valor) > 26 and int(valor) < idade:
        desconto = int(valor) - (int(valor)*0.05)
        print('Você terá um desconto de 5%, seu produto custará R$' + str(desconto))

verificar_produto(limite)
