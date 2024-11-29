#Manutenção com um count que serve como primary key e uma descrição
class ManutencaoEmergencial:
    _count = 0

    def __init__(self, descricao=""):
        self.numeroChamado = ManutencaoEmergencial._count
        self.descricao = descricao
        ManutencaoEmergencial._count += 1

    def para_dicionario(self):
        return {"numeroChamado": self.numeroChamado, "descricao": self.descricao}

    def do_dicionario(self, data):
        self.numeroChamado = data.get("numeroChamado", 0)
        self.descricao = data.get("descricao", "")

    def __str__(self):
        return f"Manutenção {self.numeroChamado}: {self.descricao}" if self.descricao else f"Manutenção {self.numeroChamado}: Sem manutenção ativa."


class Vaga:
    def __init__(self, numero, tipo_veiculo, tipo_tarifa, valor_tarifa):
        self.numero = numero
        self.tipo_veiculo = tipo_veiculo
        self.tipo_tarifa = tipo_tarifa
        self.valor_tarifa = valor_tarifa
        self.em_manutencao = False
        self.manutencao = None
        self.ocupada = False
    
    #Logica de ocupação e desocupação de vaga
    def ocupar_vaga(self, tipo_veiculo, tipo_tarifa):
        if self.ocupada:
            print(f"Vaga {self.numero} já está ocupada.")
            return False
        if self.em_manutencao:
            print(f"Vaga {self.numero} está em manutenção e não pode ser ocupada.")
            return False

        if self.tipo_veiculo != tipo_veiculo or self.tipo_tarifa != tipo_tarifa:
            print(f"Erro: A vaga {self.numero} não aceita esse tipo de veículo ou tarifa.")
            return False

        self.ocupada = True
        # Lógica do caixa pode ser adicionada aqui
        return True

    def desocupar_vaga(self):
        if self.ocupada:
            self.ocupada = False
            print(f"Vaga {self.numero} desocupada com sucesso.")
        else:
            print(f"Vaga {self.numero} não está ocupada.")
    
    #Logica de criação de manutenção
    def criar_manutencao(self, descricao):
        if not self.em_manutencao:
            self.manutencao = ManutencaoEmergencial(descricao)
            self.em_manutencao = True
            print(f"Manutenção na vaga {self.numero} criada com sucesso.")
        else:
            self.manutencao = None
            self.em_manutencao = False
            print(f"Manutenção na vaga {self.numero} removida com sucesso.")
    
    #Exibir a vaga
    def exibir_detalhes(self):
        detalhes = (
            f"Vaga {self.numero}: {self.tipo_veiculo}, Tarifa: {self.tipo_tarifa.capitalize()}, R$ {self.valor_tarifa:.2f}\n"
            f"{self.manutencao if self.manutencao else 'Sem manutenção.'}\n"
            f"{'Ocupada' if self.ocupada else 'Disponível'}"
        )
        return detalhes

    #Conversão em dicionário
    def para_dicionario(self):
        return {
            "numero": self.numero,
            "tipo_veiculo": self.tipo_veiculo,
            "tipo_tarifa": self.tipo_tarifa,
            "valor_tarifa": self.valor_tarifa,
            "ocupada": self.ocupada,
            "em_manutencao": self.em_manutencao,
            "manutencao": self.manutencao.para_dicionario() if self.manutencao else None
        }

    def do_dicionario(self, data):
        self.numero = data.get("numero", 0)
        self.tipo_veiculo = data.get("tipo_veiculo", "")
        self.tipo_tarifa = data.get("tipo_tarifa", "")
        self.valor_tarifa = data.get("valor_tarifa", 0.0)
        self.ocupada = data.get("ocupada", False)
        self.em_manutencao = data.get("em_manutencao", False)
        manutencao_data = data.get("manutencao", None)
        if manutencao_data:
            self.manutencao = ManutencaoEmergencial()
            self.manutencao.do_dicionario(manutencao_data)
        else:
            self.manutencao = None

class Estacionamento:
    def __init__(self):
        self.vagas = []

    def adicionar_vaga(self, tipo_veiculo, tipo_tarifa, valor_tarifa):
        numero_vaga = len(self.vagas) + 1
        nova_vaga = Vaga(numero_vaga, tipo_veiculo, tipo_tarifa, valor_tarifa)
        self.vagas.append(nova_vaga)
        print(f"Vaga {nova_vaga.numero} adicionada: {tipo_veiculo}, {tipo_tarifa.capitalize()}, R$ {valor_tarifa:.2f}.")

    def listar_vagas(self):
        for vaga in self.vagas:
            print(vaga.exibir_detalhes())

    def para_dicionario(self):
        return {
            "vagas": [vaga.exibir_detalhes() for vaga in self.vagas],
        }

    def do_dicionario(self, data):
        self.vagas = [Vaga(vaga['numero'], vaga['tipo_veiculo'], vaga['tipo_tarifa'], vaga['valor_tarifa']) for vaga in data.get("vagas", [])]
