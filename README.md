# Dados_DesafioFinal_Residencia_PortoDigital
Desafio final desenvolvido para a Residência do Porto Digital na empresa A3Data onde tivemos a oportunidade de aprender os processos de ETL e criação de dashboards com PowerBI.

## Instruções de Uso:

1. Instale as bibliotecas necessárias usando os comandos pip install pandas e pip install duckdb.
2. Execute o notebook para criar o DataFrame, executar a consulta SQL e salvar os dados em formato Parquet.

## Notas

O código está dividido em três classes principais:

1. DataframeCreator:

- Essa classe tem o propósito de criar um DataFrame a partir de um arquivo CSV.
- Permite lidar com exceções como arquivos não encontrados, arquivos vazios e erros de análise.

2. SQLExecutor:

- Uma classe para executar consultas SQL em um DataFrame usando DuckDB como backend de execução.
- Conecta-se a um banco de dados em memória, registra o DataFrame como uma tabela DuckDB e executa consultas SQL nessa tabela.

3. ParquetDataProcessor:

- Esta classe facilita o processo de salvar um DataFrame em formato Parquet.
- Inclui um método para salvar o DataFrame em um arquivo Parquet, lidando com exceções que podem ocorrer durante o processo.

O notebook também inclui a instância dessas classes, onde um DataFrame é criado a partir de um arquivo CSV online, uma consulta SQL é executada no DataFrame e, finalmente, o DataFrame é salvo em formato Parquet.


## Equipe

Bárbara Leimig: (https://github.com/BarbaraLeimig)
Carlos Campos: (https://github.com/carloscamposb)
Lucas Teixeira: (https://github.com/Lukgt)
Rodrigo Souza: (https://github.com/rodrigolsouza)         
Ruth Xavier:(https://github.com/xavierruth)