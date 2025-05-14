
while True:
    cpf_recebido = input('Digite seu cpf:\n>')
    # cpf_recebido = '74682489070'
    peso_digito1 = 10
    peso_digito2 = 11
    soma_digito1 = 0
    soma_digito2 = 0

    if not cpf_recebido.isdigit():
        print('Digite apenas números inteiros')
    elif len(cpf_recebido) != 11:
        print('Tamanho incorreto, digite 11 dígitos')
    else: 
        cpf_9digitos = cpf_recebido[:9]
        for digito1 in cpf_9digitos:
            digito1 = int(digito1) * peso_digito1
            soma_digito1 += digito1
            peso_digito1 -= 1
        soma_digito1 *= 10
        resto_soma1 = soma_digito1 % 11

        if resto_soma1 > 9:
            resto_soma1 = 0

        cpf_10digitos = cpf_9digitos + str(resto_soma1)

        for digito2 in cpf_10digitos:
            digito2 = int(digito2) * peso_digito2
            soma_digito2 += digito2
            peso_digito2 -= 1
        soma_digito2 *= 10
        resto_soma2 = soma_digito2 %11

        if resto_soma2 > 9:
            resto_soma2 = 0 

        ultimos_digitos = str(resto_soma1) + str(resto_soma2)
        if ultimos_digitos == cpf_recebido[9:]:
            print('CPF Válido')
        else:
            print('CPF Inválido')