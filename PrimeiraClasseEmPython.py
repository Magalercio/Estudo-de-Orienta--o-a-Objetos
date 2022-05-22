# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes
class TV:

    def __init__(self, largura):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = largura
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

    def mudar_volume(self):
        x= True
        while x == True:
            volume = input('Qual volume gostaria de colocar?')
            if volume.isnumeric():
                volume = int(volume)
                if 100 < volume or 0 > volume:
                    print('Volume inválido pra essa Tv, tente novamente.')
                    x = True
                else:
                    x=False
            else:
                print('Você não digitou um número.')
                x=True
        self.volume = volume



#programa
tv_sala = TV(55)
tv_quarto = TV(largura=33)

tv_sala.mudar_canal('Globo')
tv_quarto.cor = 'branca'
tv_sala.mudar_volume()

print(f'volume da tv da sala é {tv_sala.volume}')
print(tv_sala.canal)
print(tv_quarto.canal)
print(tv_sala.tamanho)
print(tv_quarto.tamanho)

