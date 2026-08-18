import pandas as pd
import numpy as np 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent



def carregar_dados(file) -> pd.DataFrame:
    """
        Funcão para carregar e gerar a DF já com a coluna vazia eliminada
    """
    caminho_arquivo = BASE_DIR/file

    print(f"Procurando o arquivo em: {caminho_arquivo}\n")
    df = pd.read_csv(caminho_arquivo, sep=';', header='infer')
    if "Unnamed: 6" in df.columns:
        df = df.drop(columns=["Unnamed: 6"])

    return df

#def emails_enviar () -> list:
    """
        Função para gerar as lista dos correios electrônicos para envia
    """
#def envio_email(df: pd.DataFrame):
 #   df = carregar_dados('Responsáveis_Balcões_Centros.csv')

  #  df_email = df.copy()
   # df_email = df_email['Correio Electrónico'].dropna().tolist()
    
    #return df_email

df = carregar_dados('Responsáveis_Balcões_Centros.csv')
print(df[['Código', 'Correio Electrónico']])
credenciais =  df[['Código', 'Correio Electrónico']].dropna()

for codigo, correio in credenciais.itertuples(index = False):
    cred = {'codigo': codigo, 'correio': correio}
    print(cred)

