import chardet  # Importar a biblioteca chardet
import pandas as pd
import os

# Caminho do arquivo
caminho_arquivo = r"C:\Users\guilh\OneDrive\Desktop\diamonds.csv"

# Verificar se o arquivo existe
if not os.path.exists(caminho_arquivo):
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    exit()

# Detectar a codificação do arquivo
try:
    with open(caminho_arquivo, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)

    # Verificar se a codificação foi detectada corretamente
    if result['encoding'] is None:
        print("Não foi possível detectar a codificação do arquivo. Usando UTF-8 como padrão.")
        encoding = 'utf-8'
    else:
        print(f"Codificação detectada: {result['encoding']}")
        encoding = result['encoding']

    # Ler o arquivo CSV com a codificação detectada
    try:
        dados = pd.read_csv(caminho_arquivo, encoding=encoding)
        print("Arquivo lido com sucesso!")
        print(dados.head())  # Exibir as primeiras linhas do arquivo
    except Exception as e:
        print(f"Erro ao ler o arquivo com a codificação '{encoding}': {e}")
        print("Tentando ler com UTF-8 como fallback...")
        try:
            dados = pd.read_csv(caminho_arquivo, encoding='utf-8')
            print("Arquivo lido com sucesso usando UTF-8!")
            print(dados.head())
        except Exception as e:
            print(f"Erro ao ler o arquivo com UTF-8: {e}")

except Exception as e:
    print(f"Erro ao detectar a codificação do arquivo: {e}")