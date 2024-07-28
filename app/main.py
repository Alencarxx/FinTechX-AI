from dotenv import load_dotenv
import os
import streamlit as st
import mysql.connector
import google.generativeai as genai
import pandas as pd

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a chave da API Genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Função para carregar o modelo Google Gemini e fornecer respostas às consultas
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    sql_query = response.text.strip()
    # Remover caracteres ou palavras adicionais indesejadas
    sql_query = sql_query.replace('```', '').strip()
    return sql_query

# Função para limpar a consulta SQL
def clean_sql_query(sql_query):
    cleaned_query = sql_query.replace("```", "").strip()
    return cleaned_query

# Função para obter o esquema do banco de dados
def get_database_schema():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("""
        SELECT table_name, column_name
        FROM information_schema.columns
        WHERE table_schema = DATABASE()
        """)
        schema = {}
        for table, column in cur.fetchall():
            if table not in schema:
                schema[table] = []
            schema[table].append(column)
        conn.close()
        return schema
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {}

# Função para gerar o prompt com o esquema do banco de dados
def generate_prompt(schema):
    prompt_lines = [
        "You are an expert in converting English questions into SQL queries for a MySQL database.",
        "Please ensure the SQL query is valid and does not include any additional explanations, comments, or characters that could cause a syntax error.",
        "The SQL query should only include valid SQL syntax and should not contain the words 'sql', '```', or any additional descriptions.",
        "",
        "The database schema is as follows:"
    ]
    for table, columns in schema.items():
        prompt_lines.append(f"- {table} ({', '.join(columns)})")
    prompt_lines.append("\nExample questions:")
    prompt_lines.append("1. What is the total quantity of products sold?")
    prompt_lines.append("   Example SQL: SELECT p.product_name, SUM(od.quantity) AS total_quantity_sold ")
    prompt_lines.append("   FROM order_details od")
    prompt_lines.append("   JOIN products p ON od.product_id = p.id")
    prompt_lines.append("   GROUP BY p.product_name;")
    prompt_lines.append("2. What is the total sales for the year 2023?")
    prompt_lines.append("   Example SQL: SELECT SUM(od.unit_price * od.quantity) AS total_sales ")
    prompt_lines.append("   FROM orders o")
    prompt_lines.append("   JOIN order_details od ON o.id = od.order_id")
    prompt_lines.append("   WHERE YEAR(o.shipped_date) = 2023;")
    return "\n".join(prompt_lines)

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

# Obter o esquema do banco de dados
schema = get_database_schema()
# Gerar o prompt com base no esquema do banco de dados
prompt = generate_prompt(schema)

# App do Streamlit
st.title("FinTechX AI")
st.write("Bem-vindo ao aplicativo FinTechX AI! Faça uma pergunta e obtenha insights do seu banco de dados.")

question = st.text_input("Digite sua pergunta:", key="input")
submit = st.button("Fazer a pergunta")

if submit:
    attempts = 0
    max_attempts = 5
    response_df = pd.DataFrame()
    while attempts < max_attempts and response_df.empty:
        sql_query = get_gemini_response(question, prompt)
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
