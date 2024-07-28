
# Explicação do codigo fonte linha a linha: Projeto FinTechX
-------------------------------------------------------------------------------

from dotenv import load_dotenv
import os
import streamlit as st
import mysql.connector
import google.generativeai as genai
import pandas as pd


# 1. from dotenv import load_dotenv: Importa a função load_dotenv da biblioteca dotenv, usada para carregar variáveis de ambiente de um arquivo .env.
# 2. import os: Importa o módulo os, que fornece funções para interagir com o sistema operacional, incluindo acesso a variáveis de ambiente.
# 3. import streamlit as st: Importa o Streamlit, uma biblioteca para criação de aplicativos web interativos em Python.
# 4. import mysql.connector: Importa o módulo mysql.connector, que permite a conexão com um banco de dados MySQL.
# 5. import google.generativeai as genai: Importa a biblioteca google.generativeai e a renomeia como genai, usada para interagir com modelos generativos da Google.
# 6. import pandas as pd: Importa o Pandas, uma biblioteca para manipulação e análise de dados.

# Carregar variáveis de ambiente
load_dotenv()

# 7. load_dotenv(): Carrega as variáveis de ambiente do arquivo .env para o ambiente de execução, tornando-as acessíveis através de os.getenv().

# Configurar a chave da API Genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 8. genai.configure(api_key=os.getenv("GOOGLE_API_KEY")): Configura a chave de API para acessar os serviços da Google Generative AI, utilizando a chave armazenada na variável de ambiente GOOGLE_API_KEY.

# Função para carregar o modelo Google Gemini e fornecer respostas às consultas
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    sql_query = response.text.strip()
    # Remover caracteres ou palavras adicionais indesejadas
    sql_query = sql_query.replace('```', '').strip()
    return sql_query

# 9. def get_gemini_response(question, prompt):: Define uma função para gerar uma consulta SQL a partir de uma pergunta em linguagem natural.
# 10. model = genai.GenerativeModel('gemini-pro'): Instancia o modelo gemini-pro da Google Generative AI.
# 11. response = model.generate_content([prompt[0], question]): Gera uma resposta do modelo usando o prompt e a question fornecida.
# 12. sql_query = response.text.strip(): Obtém o texto da resposta e remove espaços em branco no início e no final.
# 13. sql_query = sql_query.replace('```', '').strip(): Remove caracteres indesejados (```) da consulta gerada e limpa espaços adicionais.
# 14. return sql_query: Retorna a consulta SQL gerada.

# Função para limpar a consulta SQL
def clean_sql_query(sql_query):
    cleaned_query = sql_query.replace("```", "").strip()
    return cleaned_query

# 15. def clean_sql_query(sql_query):: Define uma função para limpar a consulta SQL gerada.
# 16. cleaned_query = sql_query.replace("```", "").strip(): Remove caracteres indesejados e limpa espaços em branco.
# 17. return cleaned_query: Retorna a consulta SQL limpa.

# Função para executar a consulta SQL no banco de dados MySQL
def read_sql_query(sql):
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cleaned_sql = clean_sql_query(sql)
        print("Executing SQL Query:", cleaned_sql)
        cur.execute(cleaned_sql)
        rows = cur.fetchall()
        column_names = [desc[0] for desc in cur.description] if cur.description else []
        conn.close()
        print("Query Results:", rows)
        
        df = pd.DataFrame(rows, columns=column_names)
        return df
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return pd.DataFrame()

# 18. def read_sql_query(sql):: Define uma função para executar uma consulta SQL no banco de dados MySQL.
# 19. try:: Inicia um bloco de código que tentará conectar ao banco de dados e executar a consulta.
# 20. conn = mysql.connector.connect(...): Conecta ao banco de dados MySQL usando as variáveis de ambiente para o host, usuário, senha e nome do banco de dados.
# 21. cur = conn.cursor(): Cria um cursor para executar consultas SQL.
# 22. cleaned_sql = clean_sql_query(sql): Limpa a consulta SQL utilizando a função clean_sql_query.
# 23. print("Executing SQL Query:", cleaned_sql): Imprime a consulta SQL que será executada.
# 24. cur.execute(cleaned_sql): Executa a consulta SQL no banco de dados.
# 25. rows = cur.fetchall(): Recupera todos os resultados da consulta.
# 26. column_names = [desc[0] for desc in cur.description] if cur.description else []: Obtém os nomes das colunas dos resultados, se houver.
# 27. conn.close(): Fecha a conexão com o banco de dados.
# 28. print("Query Results:", rows): Imprime os resultados da consulta.
# 29. df = pd.DataFrame(rows, columns=column_names): Converte os resultados em um DataFrame do Pandas para fácil manipulação e exibição.
# 30. return df: Retorna o DataFrame contendo os resultados da consulta.
# 31. except mysql.connector.Error as err:: Captura exceções relacionadas ao MySQL.
# 32. print(f"Error: {err}"): Imprime a mensagem de erro.
# 33. return pd.DataFrame(): Retorna um DataFrame vazio em caso de erro.

# Defina seu prompt
prompt = [
    """
    You are an expert in converting English questions into SQL queries for a MySQL database.
    Please ensure the SQL query is valid and does not include any additional explanations, comments, or characters that could cause a syntax error.
    The SQL query should only include valid SQL syntax and should not contain the words 'sql', '```', or any additional descriptions.
    
    The database schema is as follows:
    ...
    Ensure that all tables and aliases are correctly referenced and that the SQL query is valid.
    """
]

# 34. prompt = [...]: Define o texto de prompt usado para orientar o modelo generativo na criação de consultas SQL. O prompt inclui exemplos e diretrizes para garantir que a consulta gerada seja válida.

# App do Streamlit
st.title("FinTechX AI")
st.write("Bem-vindo ao aplicativo FinTechX AI! Faça uma pergunta e obtenha insights do seu banco de dados.")

# 35. st.title("FinTechX AI"): Define o título do aplicativo Streamlit.
# 36. st.write("Bem-vindo ao aplicativo FinTechX AI! Faça uma pergunta e obtenha insights do seu banco de dados."): Exibe uma mensagem de boas-vindas e instruções aos usuários.

question = st.text_input("Digite sua pergunta:", key="input")
submit = st.button("Fazer a pergunta")

# 37. question = st.text_input("Digite sua pergunta:", key="input"): Cria um campo de entrada de texto onde o usuário pode digitar sua pergunta.
# 38. submit = st.button("Fazer a pergunta"): Cria um botão que, quando clicado, define a variável submit como True.

if submit:
    attempts = 0
    max_attempts = 5
    response_df = pd.DataFrame()
    while attempts < max_attempts and response_df.empty:
        sql_query = get_gemini_response(question, prompt)
        #st.write(f"Tentativa {attempts + 1}: Consulta SQL Gerada:", sql_query)
        try:
            response_df = read_sql_query(sql_query)
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
        attempts += 1

    if not response_df.empty:
        st.subheader("Resultado(s):")
        st.dataframe(response_df)
    else:
        st.write("Nenhum resultado encontrado após várias tentativas. Tente reformular a pergunta.")

# 39. if submit:: Executa o bloco de código abaixo se o botão de submissão foi clicado.
# 40. attempts = 0: Inicializa o contador de tentativas.
# 41. max_attempts = 5: Define o número máximo de tentativas para obter uma consulta SQL válida.
# 42. response_df = pd.DataFrame(): Inicializa um DataFrame vazio para armazenar os resultados.
# 43. while attempts < max_attempts and response_df.empty:: Loop para tentar gerar uma consulta SQL válida até atingir o número máximo de tentativas ou obter um resultado.
# 44. sql_query = get_gemini_response(question, prompt): Gera uma consulta SQL a partir da pergunta do usuário.
# 45. try:: Tenta executar a consulta SQL.
# 46. response_df = read_sql_query(sql_query): Executa a consulta SQL no banco de dados e armazena os resultados no DataFrame response_df.
# 47. except Exception as e:: Captura exceções durante a execução da consulta.
# 48. st.error(f"Ocorreu um erro: {e}"): Exibe uma mensagem de erro no aplicativo Streamlit.
# 49. attempts += 1: Incrementa o contador de tentativas.
# 50. if not response_df.empty:: Verifica se o DataFrame response_df não está vazio.
# 51. st.subheader("Resultado(s):"): Exibe um subtítulo "Resultado(s):".
# 52. st.dataframe(response_df): Exibe o DataFrame response_df no aplicativo Streamlit.
# 53. else:: Caso response_df esteja vazio após todas as tentativas.
# 54. st.write("Nenhum resultado encontrado após várias tentativas. Tente reformular a pergunta."): Exibe uma mensagem informando que nenhuma resposta foi encontrada.





