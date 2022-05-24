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
from random import randint


class ContaCorrente:
    """
    Cria um objeto conta corrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do cliente.
        cpf(str): cpf do cliente. Deve ser inserido com ponto e traços.
        agencia(int): agência responsável pela conta do cliente.
        num_conta(int): Número da conta do cliente.
        saldo(flt): saldo disponível na conta do cliente.
        _limite(flt): _limite do cheque especial da conta do cliente.
        transações(list): Histórico de transações da conta do cliente, com descrição de tipo, quantidade, data e hora.
        cartões(list): Lista dos cartões disponíveis para essa conta. Vinculado com a Classe CartoesCredito.
    """

    @staticmethod
    def _data_hora():
        """
        Função auxiliar que passa data e hora com fuso horário brasileiro.
        :return: Retorno de data e hora atual.
        """
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now (fuso_BR)
        return horario_BR.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia,num_conta):
        self.nome = nome
        self._cpf = cpf
        self._saldo = 0.00
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes =[]
        self.cartoes = []




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
            Remove valor da conta do cliente, através de um saque, caso haja saldo _limite suficiente para saque.
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
           Consulta qual o _limite do cheque especial da conta do cliente.
           Não há parâmetros necessários.
        """
        print(f'Seu _limite de cheque especial é de R${self._limite_conta():,.2f}')

    def consulta_historico_transacoes(self):
        """
            Consulta o histórico de transações da conta do cliente, retornando: tipo, valor,saldo, data e hora.
            Não há parâmetros necessários.
        """
        print('-' * 70)
        print(f'Histórico de Transações de {self.nome}:')
        for transacao in self._transacoes:
            print(transacao)
        print('-'*70)

    def transferir(self, valor, conta_destino):
        """
            Executa uma transferência de uma conta para a outra, caso haja saldo _limite suficiente para a transferência.
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
            print(f'Transferencia para {conta_destino.nome} concluída com sucesso no valor de R${valor:,.2f}')
            self._saldo -= valor
        self._transacoes.append(('Transferência', -valor, f'Saldo R${self._saldo}', ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append(('Transferência', valor, f'Saldo R${conta_destino._saldo}', ContaCorrente._data_hora()))

class CartaoCredito:
    """
       Cria um objeto cartão de crédito para gerenciar os cartões dos clientes.

       Atributos:
           numero (int): numero do cartão.
           titular(str): Nome do titular do cartão.
           validade(str): Data de validade do cartão.
           cod_seguranca(str): código de segurança do cartão.
           limite(flt): limite de crédito do cartão.
           senha(str): Senha numérica do cartão.
           conta_corrente(int): Numero da conta corrente relacionada, ligada diretamente com a Classe ContaCorrente.
       """

    @staticmethod
    def _data_hora():
        """
        Função auxiliar que passa data e hora com fuso horário brasileiro.
        :return: Retorno de data e hora não formatado..
        """
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self,titular,conta_corrente):
        self._numero = randint (1000000000000000, 9999999999999999)
        self.titular = titular
        self._validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self._cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self._limite = 1000
        self._senha = "1234"
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        """
        Getter da senha do cartão de crédito.
        :return: senha.
        """
        return self._senha

    @senha.setter
    def senha(self, valor):
        """
        Setter da senha do cartão de crédito.
        :param valor: nova senha do cartão de crédito.
        :return: nova senha caso esteja dentro do parametro de quatro digitos numéricos.
        """
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print('Senha alterada com sucesso.')
        else:
            print("Nova senha inválida!")


