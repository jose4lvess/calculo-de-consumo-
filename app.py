print("=== Calculadora de Consumo de Energia ===")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Digite o tempo de uso diário (em horas): "))

# cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# custo estimado (opcional)
valor_kwh = 0.75
custo = consumo_mensal * valor_kwh

print("\n=== Resultado ===")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}")
