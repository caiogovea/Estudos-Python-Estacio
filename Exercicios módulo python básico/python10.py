print("Qual distância total da viagem?: ")
distancia = float(input())

print("Qual consumo médio do seu veículo por km?: ")
consumoM = float(input())

print("Qual preço atual do litro do combustivel na sua localidade?: ")
precoC = float(input())

print("Qual quantidade de pedágios até o seu destino final?: ")
qtPedagios = int(input())

print("Qual valor médio de cada pedágio?: ")
valorPedagio = float(input())

litrosCombustivel = distancia / consumoM
print(f"Litros necessários de combustivel: {litrosCombustivel}")

custoCombustivel = litrosCombustivel * precoC
print(f"Custo total de combustivel: {custoCombustivel}")

gastoPedagios = qtPedagios * valorPedagio
print(f"Custo total de pedágios: {gastoPedagios}")

valorTotalViagem = custoCombustivel + gastoPedagios
print(f"Custo total da viagem: {valorTotalViagem}")