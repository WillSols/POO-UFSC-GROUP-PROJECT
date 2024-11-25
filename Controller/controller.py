from Model.model import ManutencaoEmergencial


class EstacionamentoController:
    def __init__(self, estacionamento):
        self.estacionamento = estacionamento

    #Criador de vaguinhas marotas.
    def adicionar_vaga(self):
        tipo_veiculo = input("Digite o tipo de veículo: ")
    
        while True:
            tipo_tarifa = input("Digite o tipo de tarifa (diária ou mensal): ").lower()
            if tipo_tarifa in ["diária", "mensal"]:
                break
            else:
                print("Tipo de tarifa inválido. Por favor, digite 'diária' ou 'mensal'.")
    
        valor_tarifa = float(input("Digite o valor da tarifa: R$ "))
    
        self.estacionamento.adicionar_vaga(tipo_veiculo, tipo_tarifa, valor_tarifa)
        print(f"Vaga adicionada com sucesso. Total de vagas: {len(self.estacionamento.vagas)}")

    
    #Exibe qual o tipo de vaga, se está disponível e se tem manutenção a descrição da manutenção.
    def exibir_vagas(self):
        if not self.estacionamento.vagas:
            print("Não há vagas cadastradas.")
        else:
            for vaga in self.estacionamento.vagas:
                print(vaga.exibir_detalhes())

    #Agregador de manutenção a vaga
    def atualizar_manutencao(self):
        vaga_numero = int(input("Digite o número da vaga para adicionar/remover manutenção: "))
        vaga = next((v for v in self.estacionamento.vagas if v.numero == vaga_numero), None)
        
        if vaga:
            descricao = input("Digite a descrição da manutenção: ")
            vaga.ocupada = True
            vaga.criar_manutencao(descricao)
            print(f"Manutenção {'adicionada' if vaga.em_manutencao else 'removida'} na vaga {vaga.numero}.")
        else:
            print(f"Vaga {vaga_numero} não encontrada.")
    
    #Editor de vagas, vê se a vaga existe e se ela está ocupada ou não no momento da edição
    def editar_vaga(self):
        vaga_numero = int(input("Digite o número da vaga que deseja editar: "))
        vaga = next((v for v in self.estacionamento.vagas if v.numero == vaga_numero), None)

        if vaga: 
            if not vaga.ocupada: 
                print(f"Vaga {vaga.numero} encontrada. Detalhes atuais: {vaga.exibir_detalhes()}")

                tipo_veiculo = input(f"Digite o novo tipo de veículo (atualmente: {vaga.tipo_veiculo}): ")
                while True:
                    tipo_tarifa = input(f"Digite o novo tipo de tarifa (atualmente: {vaga.tipo_tarifa}): ").lower()
                    if tipo_tarifa in ["diária", "mensal"]:
                        break
                    else:
                        print("Tipo de tarifa inválido. Por favor, digite 'diária' ou 'mensal'.")

                valor_tarifa = float(input(f"Digite o novo valor da tarifa (atualmente: R$ {vaga.valor_tarifa}): R$ "))

                vaga.tipo_veiculo = tipo_veiculo
                vaga.tipo_tarifa = tipo_tarifa
                vaga.valor_tarifa = valor_tarifa

                print(f"Vaga {vaga.numero} atualizada com sucesso.")
                print(f"Novo detalhe da vaga: {vaga.exibir_detalhes()}")
            else:
                print(f"Vaga {vaga_numero} está ocupada e não pode ser editada.")
        else:
            print(f"Vaga {vaga_numero} não encontrada.")



    def ocupar_vaga(self):
        vaga_numero = int(input("Digite o número da vaga para ocupar: "))
        tipo_veiculo = input("Digite o tipo de veículo que vai ocupar a vaga: ")
        tipo_tarifa = input("Digite o tipo de tarifa que será aplicado: ").lower()

        vaga = next((v for v in self.estacionamento.vagas if v.numero == vaga_numero), None)
    
        if vaga:
            if vaga.em_manutencao:
                print(f"Vaga {vaga.numero} está em manutenção e não pode ser ocupada.")
                return
        
            if vaga.ocupar_vaga(tipo_veiculo, tipo_tarifa):
                print(f"Vaga {vaga.numero} ocupada com sucesso.")
            
                if vaga.manutencao:
                    vaga.criar_manutencao("")
            else:
                print(f"Erro ao tentar ocupar a vaga {vaga.numero}.")
        else:
            print(f"Vaga {vaga_numero} não encontrada.")


    def desocupar_vaga(self):
        vaga_numero = int(input("Digite o número da vaga para desocupar: "))
        vaga = next((v for v in self.estacionamento.vagas if v.numero == vaga_numero), None)
        
        if vaga:
            if vaga.em_manutencao:
                print(f"Removendo manutenção da vaga {vaga.numero}.")
                vaga.manutencao = None
                vaga.em_manutencao = False
                ManutencaoEmergencial._count -= 1
            vaga.desocupar_vaga()
        else:
            print(f"Vaga {vaga_numero} não encontrada.")

    def salvar_em_dicionario(self):
        return self.estacionamento.para_dicionario()

    def carregar_de_dicionario(self, dados):
        self.estacionamento.do_dicionario(dados)

    #Menu interativo, adicionar opções aqui.
    def menu(self):
        while True:
            print("\n=== MENU DO ESTACIONAMENTO ===")
            print("1. Adicionar vaga")
            print("2. Editar vaga")
            print("3. Exibir vagas")
            print("4. Atualizar manutenção em vaga específica")
            print("5. Ocupar vaga")
            print("6. Desocupar vaga")
            print("7. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.adicionar_vaga()
            elif escolha == "2":
                self.editar_vaga()
            elif escolha == "3":
                self.exibir_vagas()
            elif escolha == "4":
                self.atualizar_manutencao()
            elif escolha == "5":
                self.ocupar_vaga()
            elif escolha == "6":
                self.desocupar_vaga()
            elif escolha == "7":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
