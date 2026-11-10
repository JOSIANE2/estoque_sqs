from decimal import Decimal, InvalidOperation


def inteiro(valor, minimo=0):
    texto = str(valor).strip()
    try:
        numero = int(texto)
    except (ValueError, TypeError):
        raise ValueError("Informe uma quantidade inteira.") from None
    if numero < minimo:
        raise ValueError(f"A quantidade deve ser pelo menos {minimo}.")
    return numero


def dados_produto(nome, quantidade, preco):
    nome = nome.strip()
    if not nome or len(nome) > 255:
        raise ValueError("Informe um nome entre 1 e 255 caracteres.")
    quantidade = inteiro(quantidade)
    try:
        preco = Decimal(str(preco).strip().replace(",", "."))
    except InvalidOperation:
        raise ValueError("Informe um preço válido.") from None
    if not preco.is_finite() or preco < 0 or preco > Decimal("9999999999.99"):
        raise ValueError("Informe um preço não negativo dentro do limite do banco.")
    if preco != preco.quantize(Decimal("0.01")):
        raise ValueError("O preço deve ter no máximo duas casas decimais.")
    return nome, quantidade, preco
