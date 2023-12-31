# -*- coding: utf-8 -*-
"""Desafio_Final_A3DATA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ESAmv5tAS4n56X7OamVp03osPei2resr """


# CLASSE PARA CRIAÇÃO DO DATAFRAME

#pip install pandas
#pip install duckdb

import pandas as pd

class DataframeCreator:
  def __init__(self, csv_path):
    self.csv_path = csv_path

  def create_dataframe(self):
    #Lendo um arquivo csv com pandas
    try:
      dataframe = pd.read_csv(self.csv_path, encoding='latin-1', sep=',')
      return dataframe

    except FileNotFoundError:
      print(f"O arquivo não foi encontrado: {self.csv_path}")
      return None

    except pd.errors.EmptyDataError:
      print(f"O arquico está vazio: {self.csv_path}")
      return None

    except pd.errors.ParserError as e:
      print(f"Erro ao analisar o arquivo: {e}")
      return None


# CALSSE PARA CONSULTA SQL NO DATAFRAME USANDO O DUCKDB COMO BACKEND DE EXECUÇÃO

import duckdb

class SQLExecutor:
    def __init__(self, df):
        self.df = df

    def execute_sql(self, sql_script):
        # Criar uma conexão DuckDB usando o DataFrame
        con = duckdb.connect(database=':memory:',read_only=False)

        # Registrar o DataFrame como uma tabela DuckDB
        con.register('table_dataframe', self.df)

        # Executar o script SQL na tabela registrada
        result_dataframe = con.execute(sql_script).fetchdf()

        return result_dataframe


# CLASSE PARA SALVAR O DATAFRAME O DATAFRAME EM FORMATO PARQUET,FACILITANDO REUTILIZAÇÃO E MANUTENÇÃO DO CÓDIGO

class ParquetDataProcessor:
  def __init__(self, dataframe):
    self.dataframe = dataframe

  def save_to_parquet(self, output_file_path):
    try:
      self.dataframe.to_parquet(output_file_path, index=False)
      print(f"O Dataframe foi salvo em parquet: {output_file_path}")

    except Exception as e:
      print(f"Erro ao salvar o Dataframe em parquet: {e}")


#INSTACIANDO O OBJETO PARA CRIAÇÃO DO DATAFRAME

csv_path = f'https://drive.google.com/uc?export=download&id=1p34yZ2KdgClf70KhopAxE5mA-7pArvFb'

dataframe_creator = DataframeCreator(csv_path)
df = dataframe_creator.create_dataframe()

if df is not None:
  print("Dataframe criado com sucesso")
  print(df.head())
  print(df.shape)


# Query SQL

sql_script = """
SELECT
    ano as "Ano",
    estado as "Estado",
    sexo as "Sexo",
    ocup as "Ocupação",
    assistmed as "Assistência Médica",
FROM
    table_dataframe
WHERE
    ano like 2018
"""

sql_executor = SQLExecutor(df)
result_query = sql_executor.execute_sql(sql_script)

if result_query is not None:
  print(result_query.head())
  print(result_query.shape)


# INSTANCIANDO O OBJETO PARA ESCREVER E SALVAR O ARQUIVO NO FORMATO PARQUET
processor = ParquetDataProcessor(df)

processor.save_to_parquet('datasus_suicidio_2014_2018.parquet')