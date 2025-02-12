def atualizar(entidade: str, identificador: int) -> None:
    try:
        from model.tabela_ + entidade +.CRUD import select, update
        dados = select (identificador)
        # Mostrar dados existentes e pedir novos dados ao usuário.
        update(identificador, campos, novos_valores)
    except Exception:
        pass