from emails.database import conectar_bd
import pandas as pd
import numpy as np
import os
from datetime import date


hoje_str = date.today().strftime("%Y%m%d")

df = conectar_bd()

def guardar_pasta():
    # Garantir que a pasta "Arquivo" existe (cria se não existir)
    os.makedirs("Arquivo", exist_ok=True)
    
    pasta_destino = os.path.abspath("Arquivo")
    nome_arquivo = f"vendas_{hoje_str}.xlsx"
    
    # os.path.join garante a barra correta entre a pasta e o arquivo
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    # Salva o arquivo Excel
    df.to_excel(caminho_completo, index=False)
    
    return caminho_completo