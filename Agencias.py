from random import randint

class Agencia:
    """
    Cria um objeto com as agências do nosso programa bancário.

    Atributos:
        telefone (str): telefone da agencia.
        cnpj (str): cnpj da agência. Deve ser inserido com ponto e traços.
        numero (int): código da agência.
        clientes (list): Lista de clientes da agência.
        caixa (flt): saldo em caixa da agência.
        emprestimos (list): lista de empréstimos da agência.
    """
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self. cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self. caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        """
        Verifica se o saldo em caixa da agência está dentro dos parâmetros definidos.
        """
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa atual: R${self.caixa:,.2f}.')
        else:
            print(f'O valor de Caixa está OK. Caixa atual R${self.caixa:,.2f}.')

    def emprestar_dinheiro(self,valor, cpf, juros):
        """
        Realiza um emprestimo pessoal para uma pessoa.
        :param valor (flt): Valor a ser emprestado.
        :param cpf (str): Cpf do solicitante do empréstimo, deve ser adcionado com pontos e hífem.
        :param juros (flt): Juros que será cobrado pelo empréstimo.
        """
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print(f'Emprestimo realizado com sucesso no valor de R${valor:,.2f}. para o cpf: {cpf}, com juros de: {juros}')
            self.caixa -= valor
        else:
            print('Não foi possível realizar o empréstimo, valor indisponível em caixa.')

    def adcionar_cliente(self, nome, cpf, patrimonio):
        """
        Adciona um cliente à agencia.
        :param nome (str): Nome do cliente.
        :param cpf (str): cpf do cliente, deve ser adcionado com pontos e hífem.
        :param patrimonio (flt): Valor patrimonial do cliente.
        """
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    """
    Cria uma sub-classe do objeto Agencia.
    Atributos:
        site (str): Site da agência virtual. (atributo único da classe)
        telefone (str): telefone da agencia. (atributo herdado da super classe)
        cnpj (str): cnpj da agência. Deve ser inserido com ponto e traços. (atributo herdado da super classe)
        numero (int): código da agência. Definido como 1000 para todas agencias virtuais. (atributo herdado da super classe)
        clientes (list): Lista de clientes da agência. (atributo herdado da super classe)
        caixa (flt): saldo em caixa da agência. (atributo herdado da super classe)
        emprestimos (list): lista de empréstimos da agência. (atributo herdado da super classe)
        caixa_paypal (flt): Caixa da agência no aplicativo da Paypal. (atributo único da classe)

    """
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal (self, valor):
        """
            Retira dinheiro do caixa da agência.
            Adciona dinheiro na caixa da PayPal
            :param valor (flt): valor da transêrencia.
        """
        if valor > self.caixa:
            print(f"Saldo indisponível para essa transferência, Saldo no caixa da agência: R${self.caixa:,.2f}")
        else:
            print (f'Valor de R${valor:,.2f} transferido com sucesso para a PayPal.')
            self.caixa-= valor
            self.caixa_paypal+=valor

    def sacar_paypal (self, valor):
        """
            Retira dinheiro do caixa da PayPal.
            Adciona dinheiro na caixa da agência.
            :param valor (flt): valor da transêrencia.
        """
        if valor > self.caixa_paypal:
            print(f"Saldo indisponível para essa transferência, Saldo no caixa da PayPal: R${self.caixa_paypal:,.2f}")
        else:
            print (f'Valor de R${valor:,.2f} transferido com sucesso para o caixa da agência.')
            self.caixa+= valor
            self.caixa_paypal-=valor


class AgenciaComum(Agencia):
    """
        Cria uma sub-classe do objeto Agencia.
        Atributos:
            telefone (str): telefone da agencia. (atributo herdado da super classe)
            cnpj (str): cnpj da agência. Deve ser inserido com ponto e traços. (atributo herdado da super classe)
            numero (int): código da agência. Gerado aleatoriamente. (atributo herdado da super classe)
            clientes (list): Lista de clientes da agência. (atributo herdado da super classe)
            caixa (flt): saldo em caixa da agência. (atributo herdado da super classe)
            emprestimos (list): lista de empréstimos da agência. (atributo herdado da super classe)
    """
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero= randint(1001,9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    """
      Cria uma sub-classe do objeto Agencia.
      Atributos:
        telefone (str): telefone da agencia. (atributo herdado da super classe)
        cnpj (str): cnpj da agência. Deve ser inserido com ponto e traços. (atributo herdado da super classe)
        numero (int): código da agência. Gerado aleatoriamente. (atributo herdado da super classe)
        clientes (list): Lista de clientes da agência. (atributo herdado da super classe)
        caixa (flt): saldo em caixa da agência. (atributo herdado da super classe)
        emprestimos (list): lista de empréstimos da agência. (atributo herdado da super classe)
    """

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adcionar_cliente (self, nome, cpf, patrimonio):
        """
        Adciona um cliente à agencia, caso tenha patrimonio necessário para agencia premium.
        Método polimorfado da superclasse.
        :param nome (str): Nome do cliente.
        :param cpf (str): cpf do cliente, deve ser adcionado com pontos e hífem.
        :param patrimonio (flt): Valor patrimonial do cliente. Deve ser maior que um milhão para ser eletivo.
        """
        if patrimonio > 1000000:
            super().adcionar_cliente(nome,cpf,patrimonio)
            print(f"Seja bem vindo {nome} a agência Premium.")
        else:
            print('O cliente não tem o patrimônio necessário para entrar na agência Premium')


if __name__ == '__main__':
    #essa linha de comando acima faz com oq esteja aqui identado, no caso as linhas de testes, não seja rodado quando o
    #arquivo for importado para o main.py. Para caso esqueça de apagar os testes.