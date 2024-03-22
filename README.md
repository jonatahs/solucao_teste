# Comentários e Explicações da Solução Solicitada

## Entrega - 1

Neste primeiro entregável, foi solicitado um relatório relatando algumas anomalias e insights referentes ao dataset fornecido. Para essa tarefa, optou-se por utilizar o Power BI, uma ferramenta amplamente utilizada no mercado devido à sua capacidade de visualização de dados e geração de insights.

### Passos Realizados:

1. **Preparação de Dados no Power BI:** Foram realizados tratamentos na base de dados dentro do Power BI, incluindo limpeza e transformação de dados conforme necessário.
  
2. **Modelagem Dimensional:** Utilizando o conceito de Star Schema, foi desenvolvida uma modelagem dimensional no projeto do Power BI. Esse modelo permite uma organização eficiente dos dados e facilita a análise.

3. **Desenvolvimento de Dashboard:** Um dashboard foi criado para apresentar as principais tendências e insights dos dados fornecidos. Isso inclui gráficos, tabelas dinâmicas e outros elementos visuais para uma compreensão mais clara dos dados.

### Resultados:

O dashboard desenvolvido apresenta uma visualização clara e concisa das principais tendências e insights dos dados, possibilitando uma análise mais profunda e tomada de decisões informadas.<br><br>

Caso deseje visualizar o resultado final do Dashboard é possível visualiza-lo <a href = "http://surl.li/rvpsv"> CLICANDO AQUI ! </a>, caso deseje visualizar o projeto o mesmo está na pasta chamada 1-entrega

### Modelagem Star Schema adotado no Power BI
![image](https://github.com/jonatahs/solucao_teste/assets/55710320/f6bdcb80-405c-4647-a08b-974247a634b7)

## Entrega - 2

No segundo desafio, foi solicitado o tratamento de um arquivo JSON com alguns critérios específicos, incluindo a expansão de colunas em um único DataFrame e a normalização de itens. Para essa tarefa, foi escolhida a linguagem Python, aproveitando os benefícios da orientação a objetos e boas práticas de programação.

### Passos Realizados:

1. **Tratamento do Arquivo JSON:** Utilizando Python, o arquivo JSON foi tratado conforme os critérios estabelecidos, incluindo a expansão de colunas em um único DataFrame e a normalização de itens.

2. **Exportação para CSV:** Cada DataFrame resultante foi exportado para um arquivo CSV separado. Isso facilita o compartilhamento e a análise dos dados.

### Alternativas:

Além da exportação para CSV, outras opções de armazenamento e análise dos dados poderiam ser consideradas, como a utilização de arquivos Parquet para armazenamento eficiente ou a inserção direta dos dados em um banco de dados para consulta posterior.

## Entrega - 3
No terceito desafio foi proposto para desenvolver uma arquitura como fonte inicial uma API se embaseando no JSON da atividade anterior.

### Arquitetura 
![arquitetura_diagrama](https://github.com/jonatahs/solucao_teste/assets/55710320/30e8bc4e-2a91-4182-a638-9621b810a43e)

1. **Fonte inicial**: Aqui encontra-se a fonte inicial, sendo ela uma API retornando dados no formato JSON.
2. **Extract and Load**: Nesta fase, foi decidido usar o Azure Data Factory integrando com o API e carregando os dados em seu formato bruto no Azure Data Lake Storage Gen2
3. **Transform and load**: Está fase será responsável pela transformação dos dados, ou seja, vamos transformar os dados semi-estruturados para o formato estrutura utilizando Azure Databricks e carregando os dados em um Pool de SQL Dedicado no Azure Synapse Analytics, aqui será possível montar o Data Warehouse seguindo o modelo dimensional.
4. **Visualization**: Conforme o Data Warehouse foi desenvolvido atendendo o modelo dimensional e com os dados carregados, vamos integrar com o Power BI para que seja possível apresentar as analises, tendencias e insights de forma visual e interativa.<br><br>
   **Machine Learnind**: Com os dados tratados em sua forma estruturada, é possível aproveitarmos a arquitetura carregando os dados em um banco de dados no Azure Synapse Analytics, tratando e padronizando-os para atender o algoritmo de machine learning, onde iremos treinar o modelo.
5. **Analytical Workload**: Conforme os dados foram implementados no algoritmo de machine learning, iremos armazenar os resultados em outro banco de dados no Azure Synapse.
6. **Visualization**: Após a carga dos dados no banco de dados do Azure Synapse, com os resultados de machine learning, vamos integra-lo com o Power BI para apresentar os resultados da análise preditiva.
