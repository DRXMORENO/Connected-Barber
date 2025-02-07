def formatar_telefone(numero: str, estado: str, pais: str = "+55") -> str:
    
    # Remove espaços e caracteres desnecessários
    numero = ''.join(filter(str.isdigit, numero))
    estado = ''.join(filter(str.isdigit, estado))
    
    # Validação dos parâmetros
    if len(pais) < 2 or not pais.startswith('+'):
        raise ValueError("O código do país deve começar com '+' e ter pelo menos dois caracteres.")
    if len(estado) != 2 or not estado.isdigit():
        raise ValueError("O DDD deve conter exatamente 2 dígitos numéricos.")
    if len(numero) != 9 or not numero.isdigit():
        raise ValueError("O número de telefone deve conter exatamente 9 dígitos (sem formatação).")
 
    # Formatação do número
    return f"{pais} ({estado}) {numero[0]} {numero[1:5]}-{numero[5:]}"

# Exemplo de uso:
numero_formatado = formatar_telefone(numero="987654321", estado="11")
print(numero_formatado)  # Saída: +55 (11) 9 8765-4321
