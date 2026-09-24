import json
import csv


from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract
print('Iniciando a etapa de extração dos dados...\n')

dados_empresaA = Dados(path_json, 'json')
print('Nomes das colunas Empresa A:\n')

for coluna in dados_empresaA.nomes_colunas:
    print('-', coluna)

print(f'\nQuantidade de registros empresa A: {dados_empresaA.qtd_linhas} registros')

dados_empresaB = Dados(path_csv, 'csv')

print('\nNomes das colunas da Empresa B:\n')
for i in dados_empresaB.nomes_colunas:
    print('-', i)

print(f'\nQuantidade de registros empresa B: {dados_empresaB.qtd_linhas} registros')


# Transform

print('\nIniciando a etapa de transformação dos dados...\n')

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categorida do Produto',
                'Valor em Reais (R$)': 'Preco do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
print('Renomeando as colunas da empresa B...\n')
dados_empresaB.rename_columns(key_mapping)
print('Nomes das colunas da empresa B após o rename das colunas: ')
for coluna in dados_empresaB.nomes_colunas:
    print('-', coluna)

print(f'\nQuantidade de registros da empresa B após o rename das colunas: {dados_empresaB.qtd_linhas}')

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)

print('Nome das colunas após o processo de fusão dos dados:\n')
for coluna in dados_fusao.nomes_colunas:
    print('-', coluna)

print(f'\nQuantidade de registros após a fusão dos dados: {dados_fusao.qtd_linhas} registros')

# Load
print('\nIniciando a etapa de salvamento do arquivo processado...')

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f'\nOs dados foram salvos na pasta: {path_dados_combinados}')
print('\nPipeline Finalizado com sucesso!')