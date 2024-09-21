# Modelagem de Dashboard de E-commerce com Power BI

## Descrição

Este projeto consiste na criação de um modelo dimensional (esquema estrela) para um dashboard de e-commerce utilizando Power BI e fórmulas DAX. O objetivo é fornecer insights detalhados sobre as vendas, produtos, e descontos em um ambiente de e-commerce.

## Estrutura do Projeto

O projeto está dividido nas seguintes etapas:

1. **Importação dos Dados**
   - A tabela `Financial Sample` foi importada e renomeada para `Financials_origem`, sendo mantida oculta para organização do modelo.

2. **Criação das Tabelas de Dimensão**
   - **`D_Produtos`**: Contém informações sobre os produtos, incluindo ID, nomes, médias e valores de venda.
   - **`D_Produtos_Detalhes`**: Detalhes adicionais dos produtos.
   - **`D_Descontos`**: Contém as informações sobre ID, desconto e faixa de desconto.
   - **`D_Calendário`**: Tabela de datas criada com a função `CALENDAR()` para apoiar análises temporais.
   - **`D_Detalhes`**: Fornece informações adicionais sobre vendas, como regionais e representantes.

3. **Criação da Tabela Fato**
   - **`F_Vendas`**: Principal tabela de fatos contendo os dados de vendas e as chaves de ligação para as tabelas de dimensão.

## Funcionalidades e Fórmulas DAX Utilizadas

- **Cálculo de ID de produto**: Realizado com a função `RANKX` para identificar a posição dos produtos.
- **Cálculos Estatísticos**: Incluem médias, medianas, máximos e mínimos para análise de desempenho.
- **Tabela de Calendário**: Criada com a função `CALENDAR()` para suportar segmentação temporal dos dados.