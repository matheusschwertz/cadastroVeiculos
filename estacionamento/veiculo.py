class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = 29
        self.vetor = [None] * tamanho
        self.tamanho_atual = 0

    def funcao_hash(self, placa):
        soma_ascii = sum(ord(c) for c in placa)
        return soma_ascii % self.tamanho

    def buscar_posicao(self, placa):
        posicao = self.funcao_hash(placa)
        tentativas = 0
        while self.vetor[posicao] is not None and self.vetor[posicao][0] != placa and tentativas < self.tamanho:
            posicao = (posicao + 1) % self.tamanho
            tentativas += 1
        if self.vetor[posicao] is not None and self.vetor[posicao][0] == placa:
            return posicao
        else:
            return None

    def inserir(self, placa, ano, marca_modelo, cor):
        posicao = self.funcao_hash(placa)
        while self.vetor[posicao] is not None:
            posicao = (posicao + 1) % self.tamanho
        self.vetor[posicao] = (placa, ano, marca_modelo, cor)
        self.tamanho_atual += 1

    def excluir(self, placa):
        posicao = self.buscar_posicao(placa)
        if posicao is not None:
            self.vetor[posicao] = None
            self.tamanho_atual -= 1
            return True
        else:
            return False

    def buscar(self, placa):
        posicao = self.buscar_posicao(placa)
        if posicao is not None:
            return self.vetor[posicao]
        else:
            return None

    def mostrar(self):
        for i in range(self.tamanho):
            print(f"{i}: {self.vetor[i]}")

tabela = TabelaHash(29)



##     INNSERÇÃO DE 10 VEÍCULOS    ##

tabela.inserir(placa = "ISS269", ano = 2015, marca_modelo = "Audi A3", cor = "Branco")
assert tabela.buscar("ISS269")

tabela.inserir(placa = "ISS260", ano = 2022, marca_modelo = "Ford Fiesta", cor = "Preto")
assert tabela.buscar("ISS260")

tabela.inserir(placa = "ISS261", ano = 2021, marca_modelo = "Toyota Hilux", cor = "Prata")
assert tabela.buscar("ISS261")

tabela.inserir(placa = "ISS262", ano = 2023, marca_modelo = "Fiat Toro", cor = "Vermelho")
assert tabela.buscar("ISS262")

tabela.inserir(placa = "ISS263", ano = 2017, marca_modelo = "Nissan Kicks", cor = "Cinza")
assert tabela.buscar("ISS263")

tabela.inserir(placa = "ISS264", ano = 2019, marca_modelo = "Honda Civic", cor = "Azul")
assert tabela.buscar("ISS264")

tabela.inserir(placa = "ISS265", ano = 2019, marca_modelo = "Volkswagen Golf GTI", cor = "Branco")
assert tabela.buscar("ISS265")

tabela.inserir(placa = "ISS266", ano = 2022, marca_modelo = "Ford Ka", cor = "Prata")
assert tabela.buscar("ISS266")

tabela.inserir(placa = "ISS267", ano = 2010, marca_modelo = "Volkswagen Polo", cor = "Verde")
assert tabela.buscar("ISS267")

tabela.inserir(placa = "ISS268", ano = 1974, marca_modelo = "Volkswagen Brasilia", cor = "Amarelo")
assert tabela.buscar("ISS268")


##   EXCLUINDO 5 VEÍCULOS   ##

tabela.excluir("ISS269") == True
tabela.excluir("ISS269") == None

tabela.excluir("ISS267") == True
tabela.excluir("ISS267") == None

tabela.excluir("ISS264") == True
tabela.excluir("ISS264") == None

tabela.excluir("ISS263") == True
tabela.excluir("ISS263") == None

tabela.excluir("ISS262") == True
tabela.excluir("ISS262") == None

tabela.excluir("ISS261") == True
tabela.excluir("ISS261") == None


##   INSERINDO 3 VEÍCULOS  ##

tabela.inserir(placa = "ISS271", ano = 1974, marca_modelo = "Chevrolet Opala", cor = "Amarelo")
assert tabela.buscar("ISS271")

tabela.inserir(placa = "ISS272", ano = 1969, marca_modelo = "Dodge Charger", cor = "Preto")
assert tabela.buscar("ISS272")

tabela.inserir(placa = "ISS273", ano = 2016, marca_modelo = "BMW I8", cor = "Branco")
assert tabela.buscar("ISS273")


while True:
    opcao = input("Escolha uma opção:\n1. Inserir item\n2. Buscar item\n3. Excluir item\n4. Mostrar tabela\n0. Sair\n")
    if opcao == "1":
        placa = input("Informe a placa do veículo: ")
        ano = input("Informe o ano do veículo: ")
        marca_modelo = input("Informe a marca e modelo do veículo: ")
        cor = input("Informe a cor do veículo: ")
        tabela.inserir(placa, ano, marca_modelo, cor)
        print("Item inserido com sucesso.")
    elif opcao == "2":
        placa = input("Informe a placa do veículo a ser buscado: ")
        item = tabela.buscar(placa)
        if item is not None:
            print(f"Item encontrado: {item}")
        else:
            print("Item não encontrado.")
    elif opcao == "3":
        placa = input("Informe a placa do item a ser excluído: ")
        if tabela.excluir(placa):
            print("Item excluído com sucesso.")
        else:
            print("Item não encontrado.")
    elif opcao == "4":
        tabela.mostrar()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
