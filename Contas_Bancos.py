#por convenção metodos que comecem com underline,
# significa que o metodo é privado da classe e nao é para ser usado fora da classe

#Por convençao nome de classe com letras maiusculas nas inicias, nome de metodos separa com underline
# Por convenção e organização separar os metodos pulando uma linha, pular duas linhas ao finalizar a classe
#Convenção para nome de atributos e Metodos:
#um underline de inicio: é um atributo não público, para ser usado dentro da classe e não deve ser editado,
# ou se for alterado que seja através de um método, não manualmente.
# dois underlines na frente: Só deve ser usado dentro da Classe, mas deixa inacessível fora da classe.
#Exemplo: print(isntancia.__atributo) daria que esse atributo nao existe

from datetime import datetime
import pytz
import time
import random



class ContaCorrente:
    """
    Cria um objeto conta corrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do cliente.
        cpf(str): cpf do cliente. Deve ser inserido com ponto e traços.
        agencia(int): agência responsável pela conta do cliente.
        num_conta(int): Número da conta do cliente.
        saldo(flt): saldo disponível na conta do cliente.
        limite(flt): limite do cheque especial da conta do cliente.
        transações(list): Histórico de transações da conta do cliente, com descrição de tipo, quantidade, data e hora.
    """
   #todas_contas = [(100000000,'conta_teste', '000.000.000-00','Conta de Teste', 1234)]

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now (fuso_BR)
        return horario_BR.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia,num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0.00
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes =[]




    def consultar_saldo(self):
        """
            Exibe o saldo atual da conta do cliente.
            Não há parâmentros necessários.
        """
        print(f'Seu saldo atual é de: R${self._saldo:,.2f}')

    def depositar(self, valor):
        """
            Deposita um valor na conta do cliente.
            Adciona essa transação no atributo transações da conta do cliente.
            :param valor: Valor a ser depositado na conta do cliente.
        """
        self._saldo += valor
        self.consultar_saldo()
        self._transacoes.append(('depósito', valor, f'Saldo R${self._saldo}', ContaCorrente._data_hora()))

    def _limite_conta(self):
        """
            Limite do cheque especial do cliente.
            Não há parâmetros necessários.
            Método interno, para verificá-lo consulte o método 'consulta_limite_especial'.
        """
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        """
            Remove valor da conta do cliente, através de um saque, caso haja saldo limite suficiente para saque.
            Adciona essa transação no atributo transações da conta do cliente.
        :param valor: Valor a ser sacado da conta do cliente.
        """
        if self._saldo - valor < self._limite_conta():
            print('Saldo insuficiente para esse saque.')
            self.consultar_saldo()
        else:
            print(f'Saque concluído com sucesso no valor de R${valor:,.2f}')
            self._saldo -= valor
            self.consultar_saldo()
        self._transacoes.append(('saque', -valor, f'Saldo R${self._saldo}', ContaCorrente._data_hora()))

    def consulta_limite_especial(self):
        """
           Consulta qual o limite do cheque especial da conta do cliente.
           Não há parâmetros necessários.
        """
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')

    def consulta_historico_transacoes(self):
        """
            Consulta o histórico de transações da conta do cliente, retornando: tipo, valor,saldo, data e hora.
            Não há parâmetros necessários.
        """
        print('-' * 70)
        print(f'Histórico de Transações de {self._nome}:')
        for transacao in self._transacoes:
            print(transacao)
        print('-'*70)

    def transferir(self, valor, conta_destino):
        """
            Executa uma transferência de uma conta para a outra, caso haja saldo limite suficiente para a transferência.
            Remove saldo da conta origem, adciona saldo na conta destino.
            Adciona essa transação no atributo transações das contas dos clientes, tanto de Origem quanto Destino.
        :param valor: valor da transferência
        :param conta_destino: variavel/nome da conta para onde se deseja transferir.
        :return:
        """
        if self._saldo - valor < self._limite_conta():
            print('Saldo insuficiente para essa transferência.')
            self.consultar_saldo()
        else:
            print(f'Transferencia para {conta_destino._nome} concluída com sucesso no valor de R${valor:,.2f}')
            self._saldo -= valor
        self._transacoes.append(('Transferência', -valor, f'Saldo R${self._saldo}', ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append(('Transferência', valor, f'Saldo R${conta_destino._saldo}', ContaCorrente._data_hora()))


# Programa Teste
#Criando conta
#Funcao de criar conta que nao deu certo por enquanto
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