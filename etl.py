import csv

path_arquivo = 'data/vendas.csv'

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:

    """
    Função que lê um arquivo CSV e retorna uma lista de dicionários.
    """

    lista = []

    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo_csv:
        # Remove espaços após vírgula para normalizar nomes das colunas.
        leitor_csv = csv.DictReader(arquivo_csv, skipinitialspace=True)
        for linha in leitor_csv:
            lista.append(linha)
    return list(lista)


def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    
    """
    Função para categorizar produtos por status = não entregue.
    """

    lista_produtos_filtrados = []

    for produto in lista:
        if produto.get('ENTREGUE') == 'False':
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados


def somar_valores_dos_produtos_nao_entregues(filtrar_produtos_nao_entregues: list[dict]) -> int:
    
    """
    Função para somar total dos valores dos produtos não entregues.
    """

    valor_total = 0

    for produto in filtrar_produtos_nao_entregues:
        valor_total += int(produto.get('PREÇO'))          
    return valor_total