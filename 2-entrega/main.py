import pandas as pd
import json
import os


class ETL_JSON:
        
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

        return df_dim_nfe, df_dim_produto, df_fato
        
if __name__ == "__main__":

    print("""
            # ********************
            #   
            #   INICIANDO ETL !!!
            #
            # ********************
          """)

    json_data                               = ETL_JSON().busca_arquivo()
    trata_arquivo_json                      = ETL_JSON().trata_arquivo_json(json_data)
    print("""
            # ********************
            #   
            #   ARQUIVO JSON TRATADO !!!
            #
            # ********************
          """)
    df                                      = ETL_JSON().gera_dataframe(trata_arquivo_json)
    df_dim_nfe, df_dim_produto, df_fato     = ETL_JSON().gerando_modelo_dimensional(df)

    print("""
            # ********************
            #   
            #   DATAFRAMES GERADOS !!!
            #
            # ********************
          """)

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

    print("""
            # ********************
            #   
            #   ETL FINALIZADO COM SUCESSO !!!
            #
            # ********************
          """)