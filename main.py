from Contas_Bancos import ContaCorrente, CartaoCredito
import time


# Programa Teste
#Criando conta
#Funcao de criar conta (que nao deu certo por enquanto)
"""def criar_conta():

    nome1 = input('Digite o nome do cliente:')
    cpf1= input('Digite o cpf do cliente com pontos e traços, conforme aparece no documento:')
    agencia1 = int(input('Digite em qual agencia a conta será aberta:'))
    alias1 = input('Digite um apelido para a conta:')
    test_conta= True
    while test_conta==True:
        num_conta1 = int(random.randint(100000000,200000000))
        for item in ContaCorrente.todas_contas:
            if num_conta1 in ContaCorrente.todas_contas[0]:
                test_conta=True
            else:
                test_conta=False
    # todas_contas=[(num_conta1,alias1, cpf1, nome1, agencia1)]
    ContaCorrente.todas_contas.append((num_conta1,alias1, cpf1, nome1, agencia1))
    code = f"{alias1} = ContaCorrente('{nome1}', '{cpf1}', {agencia1}, {num_conta1})"
    print(code)
    exec(code)"""
#Criando contas

conta_Magal = ContaCorrente('Magalercio', '123.456.789-00', 1234, 403350702)
conta_Michelle = ContaCorrente ('Michelle', '789.654.013-01', 1234, 564832116)
#depositando
conta_Magal.depositar(1000)
time.sleep(3)
#sacando
conta_Magal.sacar_dinheiro(1200)
#consultando Limite
conta_Magal.consulta_limite_especial()
time.sleep(1)
#fazendo transferencia
conta_Magal.transferir(500, conta_Michelle)

conta_Magal.consulta_historico_transacoes()
conta_Michelle.consulta_historico_transacoes()

#help(ContaCorrente)

"""criar_conta()

criar_conta()


time.sleep(1)
#depositando
conta_Magal.depositar(1000)
time.sleep(3)
#sacando
conta_Magal.sacar_dinheiro(1200)
#consultando Limite
conta_Magal.consulta_limite_especial()
time.sleep(1)
conta_Magal.transferir(500, conta_Michelle)

conta_Magal.consulta_historico_transacoes()
conta_Michelle.consulta_historico_transacoes()



print(ContaCorrente.todas_contas)"""
#Criando cartao de credito
cartao_magal = CartaoCredito('Magalercio', conta_Magal)
#testando parametros cartao de credito
print(f'O número da conta do titular do cartão é: {cartao_magal.conta_corrente.num_conta}')
print(f'O número do cartão de crédito dessa conta é: {conta_Magal.cartoes[0]._numero}')
print(cartao_magal._validade)
print(cartao_magal._numero)
print(cartao_magal._cod_seguranca)

cartao_magal.senha = "1235"
print(cartao_magal.senha)

print(conta_Magal.__dict__)