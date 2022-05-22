#por convenção metodos que comecem com underline,
# significa que o metodo é privado da classe e nao é para ser usado fora da classe

#Por convençao nome de classe com letras maiusculas nas inicias, nome de metodos separa com underline
# Por convenção e organização separar os metodos pulando uma linha, pular duas linhas ao finalizar a classe


from datetime import datetime
import pytz
import time

class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now (fuso_BR)
        return horario_BR.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.00
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes =[]

    def consultar_saldo(self):
        print(f'Seu saldo atual é de: R${self.saldo:,.2f}')

    def depositar(self, valor):
        self.saldo += valor
        self.consultar_saldo()
        self.transacoes.append(('depósito',valor, f'Saldo R${self.saldo}', ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Saldo insuficiente para esse saque.')
            self.consultar_saldo()
        else:
            print(f'Saque concluído com sucesso no valor de R${valor:,.2f}')
            self.saldo -= valor
            self.consultar_saldo()
        self.transacoes.append(('saque',-valor, f'Saldo R${self.saldo}', ContaCorrente._data_hora()))

    def consulta_limite_especial(self):
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')

    def consulta_historico_transacoes(self):
        print('-' * 70)
        print(f'Histórico de Transações de {self.nome}:')
        for transacao in self.transacoes:
            print(transacao)
        print('-'*70)

    def transferir(self, valor, conta_destino):
        if self.saldo - valor < self._limite_conta():
            print('Saldo insuficiente para essa transferência.')
            self.consultar_saldo()
        else:
            print(f'Transferencia para {conta_destino.nome} concluída com sucesso no valor de R${valor:,.2f}')
            self.saldo -= valor
        self.transacoes.append(('Transferência',-valor, f'Saldo R${self.saldo}', ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append(('Transferência',valor, f'Saldo R${conta_destino.saldo}', ContaCorrente._data_hora()))


# Programa Teste
#Criando conta
conta_Magal = ContaCorrente('Magalercio', '123.456.789-00', 1234, 403350702)
conta_Michelle = ContaCorrente ('Michelle', '78965413-01', 1234, 564832116)
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