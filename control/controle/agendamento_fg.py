from datetime import datetime

# Estrutura de dados para armazenar agendamentos
agendamentos = []

# Função para adicionar agendamento
def adicionar_agendamento(cliente, funcionario, data_hora):
    agendamento = {
        'cliente': cliente,
        'funcionario': funcionario,
        'data_hora': datetime.strptime(data_hora, '%Y-%m-%d %H:%M')
    }
    agendamentos.append(agendamento)
    print("Agendamento adicionado com sucesso!")

# Função para listar agendamentos
def listar_agendamentos():
    if not agendamentos:
        print("Não há agendamentos registrados.")
        return
    
    print(f"{'Cliente':<20} {'Funcionário':<20} {'Data e Hora':<20}")
    print("-" * 60)
    
    for agendamento in agendamentos:
        print(f"{agendamento['cliente']:<20} {agendamento['funcionario']:<20} {agendamento['data_hora'].strftime('%Y-%m-%d %H:%M'):<20}")
    
# Função para listar agendamentos de um cliente específico
def listar_agendamentos_cliente(cliente):
    agendamentos_cliente = [ag for ag in agendamentos if ag['cliente'] == cliente]
    if not agendamentos_cliente:
        print(f"Nenhum agendamento encontrado para o cliente {cliente}.")
        return
    
    print(f"Agendamentos do cliente {cliente}:")
    print(f"{'Funcionário':<20} {'Data e Hora':<20}")
    print("-" * 40)
    
    for agendamento in agendamentos_cliente:
        print(f"{agendamento['funcionario']:<20} {agendamento['data_hora'].strftime('%Y-%m-%d %H:%M'):<20}")

# Função para listar agendamentos de um funcionário específico
def listar_agendamentos_funcionario(funcionario):
    agendamentos_funcionario = [ag for ag in agendamentos if ag['funcionario'] == funcionario]
    if not agendamentos_funcionario:
        print(f"Nenhum agendamento encontrado para o funcionário {funcionario}.")
        return
    
    print(f"Agendamentos do funcionário {funcionario}:")
    print(f"{'Cliente':<20} {'Data e Hora':<20}")
    print("-" * 40)
    
    for agendamento in agendamentos_funcionario:
        print(f"{agendamento['cliente']:<20} {agendamento['data_hora'].strftime('%Y-%m-%d %H:%M'):<20}")

# Listar todos os agendamentos
listar_agendamentos()

# Listar agendamentos de um cliente específico
listar_agendamentos_cliente("João")

# Listar agendamentos de um funcionário específico
listar_agendamentos_funcionario("Carlos")
