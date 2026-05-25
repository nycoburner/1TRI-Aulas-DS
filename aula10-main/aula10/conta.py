import random
class conta:
    # metodo construtor 
    def __init__(self, titular, agencia, numero):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = f"{random.radint(1000, 9999)}-{random.radint(1,9)}"
        self._cpf = _cpf
        self.__saldo = 0
        self._senha = random.radint(100000, 999999)
        self._chavepix = []

        @property
        def titular(self)
            return(self.__titular)
        @property
        def agencia(self):
            return self.__agencia
         @property
        def numero(self):
            return self.__numero
        @property
        def saldo(self):
            return self.__saldo
        @property
        def cpf(self):
            return self._cpf
        @property
        def chavepix(self):
            return self._chavepix
        @property
        def chavepix(self):
            return 

        @titular.setter
        def titular(self, novo_nome)
        self.__titular = novo_nome

    def extrato(self):
        print(f'o saldo do { self.__titular} é {self.__saldo}')

    def deposito(self, valor):
        self.__saldo = self.__saldo + valor

        def saque(self, valor)
        if valor <= self.__saldo and valor >0:
            self.__saldo = self.__saldo - valor
            print('saque efetuado com sucesso')
            else:
                print('erro ao efetuar o saque')
        def transferir(self, conta_destino, valor):
            self.__saque(valor)
            conta_destino.destino(valor)

