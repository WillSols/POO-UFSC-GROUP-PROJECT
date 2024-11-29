from Model.model import Estacionamento
from Controller.controller import EstacionamentoController

#Instanciamento do Estacionamento, iniciar a aplicação por essa página
estacionamento = Estacionamento()

controller = EstacionamentoController(estacionamento)

controller.menu()
