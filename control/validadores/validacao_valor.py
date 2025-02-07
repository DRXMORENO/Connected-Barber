def validar_valor_compra():
    while True:
        try:
            valor = float(input("Digite o valor da compra: R$ "))
            
            if valor <= 0:
                print("O valor da compra deve ser maior que zero. Tente novamente.")
            else:
                print(f"Valor da compra validado: R$ {valor:.2f}")
                break  # Sai do loop se o valor for válido
        except ValueError:
            print("Valor inválido.Por favor, insira o valor correto")
            
validar_valor_compra()