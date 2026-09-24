# Pipeline de Dados

Projeto de processamento e integração de dados de vendas de duas empresas. O pipeline realiza as etapas de extração, transformação e carregamento (ETL): lê os dados brutos em formatos JSON e CSV, padroniza os nomes das colunas, combina os registros e salva o resultado em um novo arquivo CSV.

## Funcionalidades

- Leitura de dados em JSON e CSV.
- Inspeção dos nomes das colunas e da quantidade de registros.
- Padronização dos nomes das colunas da Empresa B.
- Combinação dos dados das duas empresas.
- Preenchimento de campos ausentes com `Indisponivel`.
- Geração do arquivo processado em `data_processed/dados_combinados.csv`.

## Requisitos

- Python 3.8 ou superior.
- Não há dependências externas: o pipeline usa somente módulos da biblioteca padrão do Python (`json` e `csv`).

Para criar e ativar um ambiente virtual, execute na raiz do projeto:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows, a ativação pode ser feita com:

```powershell
venv\Scripts\activate
```

## Estrutura do projeto

```text
pipeline_dados/
├── data_raw/
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
├── data_processed/
│   └── dados_combinados.csv
├── notebooks/
│   └── exploracao.ipynb
└── scripts/
    ├── fusao_mercado_fev.py
    └── processamento_dados.py
```

## Como executar

1. Abra um terminal na raiz do projeto.
2. Ative o ambiente virtual, caso tenha criado um.
3. Execute o script principal:

```bash
python scripts/fusao_mercado_fev.py
```

No Windows, se necessário, use:

```powershell
py scripts/fusao_mercado_fev.py
```

O comando deve ser executado a partir da raiz do projeto porque o script utiliza caminhos relativos para localizar os arquivos de entrada e saída.

Ao final da execução, o arquivo processado estará disponível em:

```text
data_processed/dados_combinados.csv
```

## Fluxo do pipeline

1. **Extração:** carrega `dados_empresaA.json` e `dados_empresaB.csv`.
2. **Transformação:** renomeia as colunas da Empresa B para seguir o padrão da Empresa A e combina as listas de registros.
3. **Carregamento:** grava os dados combinados em `dados_combinados.csv`.

## Classe `Dados`

A classe `Dados`, definida em `scripts/processamento_dados.py`, centraliza as operações de leitura, transformação, combinação e salvamento dos dados. Ela aceita as fontes `json`, `csv` e `list`.

## Observação

O arquivo em `data_processed/` é gerado ou sobrescrito sempre que o pipeline é executado.