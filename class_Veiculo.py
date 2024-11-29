class Veiculo:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

    def __str__(self):
        return f"Placa: {self.placa}, Modelo: {self.modelo}"


class Carro(Veiculo):
    def __init__(self, placa, modelo, portas):
        super().__init__(placa, modelo)
        self.portas = portas

    def __str__(self):
        return f"Carro - {super().__str__()}, Portas: {self.portas}"


class Moto(Veiculo):
    def __init__(self, placa, modelo, cilindradas):
        super().__init__(placa, modelo)
        self.cilindradas = cilindradas

    def __str__(self):
        return f"Moto - {super().__str__()}, Cilindradas: {self.cilindradas}"


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, carga_maxima):
        super().__init__(placa, modelo)
        self.carga_maxima = carga_maxima

    def __str__(self):
        return f"Caminhão - {super().__str__()}, Carga Máxima: {self.carga_maxima} kg"


class Estacionamento:
    def __init__(self):
        self.vagas = []

    def adicionar_veiculo(self, veiculo):
        self.vagas.append(veiculo)
        print(f"Veículo adicionado: {veiculo}")

    def remover_veiculo(self, placa):
        for veiculo in self.vagas:
            if veiculo.placa == placa:
                self.vagas.remove(veiculo)
                print(f"Veículo removido: {veiculo}")
                return
        print(f"Veículo com placa {placa} não encontrado.")

    def listar_veiculos(self):
        if not self.vagas:
            print("Nenhum veículo no estacionamento.")
        else:
            print("Veículos no estacionamento:")
            for veiculo in self.vagas:
                print(veiculo)


# Exemplo de uso
if __name__ == "__main__":
    estacionamento = Estacionamento()

    carro = Carro("ABC-1234", "Sedan", 4)
    moto = Moto("XYZ-5678", "Esportiva", 600)
    caminhao = Caminhao("DEF-9101", "Truck", 15000)

    estacionamento.adicionar_veiculo(carro)
    estacionamento.adicionar_veiculo(moto)
    estacionamento.adicionar_veiculo(caminhao)

    estacionamento.listar_veiculos()

    estacionamento.remover_veiculo("XYZ-5678")
    estacionamento.listar_veiculos()

