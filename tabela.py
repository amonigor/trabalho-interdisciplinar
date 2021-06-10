import pandas as pd

class Tabela:
    def __init__(self, nome_arquivo, encoding = None):
        self.tb = pd.read_csv(nome_arquivo, encoding=encoding)
    
    def pegar_variaveis(self):
        return self.tb.columns
    
    def pegar_lista(self, idx):
        return self.tb.iloc[:, idx]