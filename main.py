from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_dos_produtos_nao_entregues

path_arquivo = 'data/vendas.csv'

lista_de_produtos = ler_csv(path_arquivo)
lista_produtos_filtrados = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_total = somar_valores_dos_produtos_nao_entregues(lista_produtos_filtrados)


print(f"Total de produtos vendidos: {len(lista_de_produtos)}")
print(f"Total de produtos não entregues: {len(lista_produtos_filtrados)}")
print(f"Valor total dos produtos não entregues: R$ {valor_total}")