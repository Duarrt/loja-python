print('Olá, seja bem vindo à DuarrtShop! Sou o Ramon Duarte, como posso ajudar?')
print('Iremos fazer uma análise do seu crédito, por gentileza, responda as seguintes questões: ')
cargo = input('Qual seu cargo atual?')
salario = input('Quanto você ganha neste cargo?')
datanasc = input('Qual seu ano de nascimento?')
print('Segundo os dados informados, seu cargo é ' + cargo + ', ganha R$' + salario + ' e nasceu no ano de ' + datanasc + '.')

def credito():
    id = 2021 - int(datanasc)
    cred = int(salario) * (id/1000) + 100
    print('Sua idade é de ' + str(id) + ' anos. E você terá um limite de R$' + str(cred) + '!')
    
credito()
