import pandas as pd
import json
import os


class ETL_JSON:
        
    def __init__(self):
        print("""
            # ***********************************
            #   
            #           INICIANDO ETL !!!
            #
            # ***********************************
          """)
        

    def busca_arquivo(self):

        # Buscando Arquivo JSON
        with open('data.json','r') as f:
            json_data = json.load(f)

        return json_data
    
    def trata_arquivo_json(self,json_data):

        blank_list = []
        for i in json_data:
            for product in i['ItemList']:
                blank_list.append({
                    "CreateDate"    : i["CreateDate"],
                    "EmissionDate"  : i["EmissionDate"],
                    "Discount"      : i["Discount"],
                    "NFeNumber"     : i["NFeNumber"],
                    "NFeID"         : i["NFeID"],
                    'ProductName'   : product['ProductName'],
                    "Value"         : product["Value"],
                    "Quantity"      : product["Quantity"]
                })

        print("""
            # ***********************************
            #   
            #   JSON tratado com sucesso !!!
            #
            # ***********************************
          """)

        return blank_list
    
    def gera_dataframe(self,blank_list):

        # Gerando Data frame
        df = pd.DataFrame(blank_list)

        # Tratando colunas de data
        df['CreateDate']            = pd.to_datetime(df['CreateDate'],format="ISO8601")
        df['EmissionDate']          = pd.to_datetime(df['EmissionDate'])

        return df

    def gerando_modelo_dimensional(self,df):

        # Dimensão NFE
        df_dim_nfe      = df[['NFeID','NFeNumber','EmissionDate']].drop_duplicates(subset=['NFeID'])

        # Dimensão Produto
        df_dim_produto  = df[['ProductName','Value']].drop_duplicates(subset=['ProductName'])

        # Normalizando tabela fato
        df_fato = df[['CreateDate','Discount','NFeID','ProductName','Quantity']]

        print("""
            # ***********************************
            #   
            #   Dataframes Gerado com Sucesso !!!
            #
            # ***********************************
          """)

        return df_dim_nfe, df_dim_produto, df_fato
    
    def __del__(self):
        print("""
            # ***********************************
            #   
            #   ETL FINALIZADO COM SUCESSO !!!
            #
            # ***********************************
          """)
if __name__ == "__main__":

    
    obj                                     = ETL_JSON()
    json_data                               = obj.busca_arquivo()
    trata_arquivo_json                      = obj.trata_arquivo_json(json_data)
    
    df                                      = obj.gera_dataframe(trata_arquivo_json)
    df_dim_nfe, df_dim_produto, df_fato     = obj.gerando_modelo_dimensional(df)

    

    # Caminho para os arquivos
    dim_nfe_csv = "dim_nfe.csv"
    dim_produto_csv = "dim_produto.csv"
    fato_vendas_csv = "fato_vendas.csv"

    # Verificar se os arquivos existem e remove se existem
    if os.path.exists(dim_nfe_csv):
        os.remove(dim_nfe_csv)
    if os.path.exists(dim_produto_csv):
        os.remove(dim_produto_csv)
    if os.path.exists(fato_vendas_csv):
        os.remove(fato_vendas_csv)

    # exporta para csv
    df_dim_nfe.to_csv(dim_nfe_csv, index=False)
    df_dim_produto.to_csv(dim_produto_csv, index=False)
    df_fato.to_csv(fato_vendas_csv, index=False)