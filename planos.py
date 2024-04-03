consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:

def recomendar_plano(consumo):
  if consumo <= 10:
    return "Plano Essencial Fibra - 50Mbps"
  elif consumo <= 19:
    return "Plano Prata Fibra - 100Mbps"
  else:
    return "Plano Premium Fibra - 300Mbps"

print(recomendar_plano(consumo))