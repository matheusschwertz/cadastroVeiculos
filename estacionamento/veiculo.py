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