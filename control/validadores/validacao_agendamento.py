from datetime import datetime

def validar_agendamento_chat(data_str):
    try:
        # Tenta converter a string para um objeto datetime com data e hora
        data_agendamento = datetime.strptime(data_str, '%d/%m/%Y %H:%M')

        # Verifica se a data e hora informada não são no passado
        if data_agendamento < datetime.now():
            return "O agendamento não pode ser no passado."

        # Verifica se o agendamento está dentro do horário de atendimento (exemplo: 09:00 - 18:00)
        if not (9 <= data_agendamento.hour < 18):
            return "O agendamento deve ser realizado entre 09:00 e 18:00."

        # Se todas as validações passarem
        return f"Agendamento válido para {data_agendamento.strftime('%d/%m/%Y %H:%M')}."
    
    except ValueError:
        # Caso a conversão falhe, significa que o formato está errado
        return "Formato de data e hora inválido. Por favor, use o formato dd/mm/aaaa HH:MM."

# Exemplo de uso
data = input("Digite a data e hora do agendamento (dd/mm/aaaa HH:MM): ")
resultado = validar_agendamento_chat(data)
print(resultado)
