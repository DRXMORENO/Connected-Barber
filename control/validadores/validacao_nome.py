def formatar_nome(nome, modo='capitalizar'):
    # Substitui espaços por underscores
    nome = nome.replace(" ", "_").strip()

    # Remove qualquer caractere especial (exceto o underscore)
    nome = ''.join(c for c in nome if c.isalnum() or c == '_')

    if modo == 'capitalizar':
        # Capitaliza a primeira letra de cada palavra, separada por '_'
        nome_formatado = '_'.join([palavra.capitalize() for palavra in nome.split('_')])
    elif modo == 'maiúsculas':
        # Converte o nome para maiúsculas
        nome_formatado = nome.upper()
    elif modo == 'minúsculas':
        # Converte o nome para minúsculas
        nome_formatado = nome.lower()
    else:
        # Caso o modo seja inválido, retorna o nome original
        nome_formatado = nome

    return nome_formatado