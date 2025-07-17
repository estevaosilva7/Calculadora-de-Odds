def calcular_aposta(valor_apostado: float, odd: float) -> dict:
    if valor_apostado <= 0 or odd <= 1:
        raise ValueError("O valor apostado deve ser maior que 0 e a odd deve ser maior que 1.")

    lucro_bruto = valor_apostado * odd
    lucro_liquido = lucro_bruto - valor_apostado

    return {
        "Valor Apostado (R$)": round(valor_apostado, 2),
        "Odd": round(odd, 2),
        "Lucro Bruto (R$)": round(lucro_bruto, 2),
        "Lucro Líquido (R$)": round(lucro_liquido, 2)
    }

# Exemplo de uso:
valor = float(input("Digite o valor apostado (R$): "))
odd = float(input("Digite a odd: "))

try:
    resultado = calcular_aposta(valor, odd)
    print("\n=== Resultado da Aposta ===")
    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")
except ValueError as e:
    print(f"Erro: {e}")
