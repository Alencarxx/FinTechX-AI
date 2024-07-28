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
    response = model.generate_content([prompt[0], question])
    sql_query = response.text.strip()
    # Remover caracteres ou palavras adicionais indesejadas
    sql_query = sql_query.replace('```', '').strip()
    return sql_query

# Função para limpar a consulta SQL
def clean_sql_query(sql_query):
    cleaned_query = sql_query.replace("```", "").strip()
    return cleaned_query

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

# Defina seu prompt
prompt = [
    """
    You are an expert in converting English questions into SQL queries for a MySQL database.
    Please ensure the SQL query is valid and does not include any additional explanations, comments, or characters that could cause a syntax error.
    The SQL query should only include valid SQL syntax and should not contain the words 'sql', '```', or any additional descriptions.
    
    The database schema is as follows:
    - customers (id, company, last_name, first_name, email_address, job_title, business_phone, home_phone, mobile_phone, fax_number, address, city, state_province, zip_postal_code, country_region, web_page, notes, attachments)
    - employees (id, company, last_name, first_name, email_address, job_title, business_phone, home_phone, mobile_phone, fax_number, address, city, state_province, zip_postal_code, country_region, web_page, notes, attachments)
    - orders (id, employee_id, customer_id, order_date, shipped_date, shipper_id, ship_name, ship_address, ship_city, ship_state_province, ship_zip_postal_code, ship_country_region, shipping_fee, taxes, payment_type, paid_date, notes, tax_rate, tax_status_id, status_id)
    - order_details (id, order_id, product_id, quantity, unit_price, discount, status_id, date_allocated, purchase_order_id, inventory_id)
    - products (id, product_code, product_name, description, standard_cost, list_price, reorder_level, target_level, quantity_per_unit, discontinued, minimum_reorder_quantity, category, attachments)
    - shippers (id, company, last_name, first_name, email_address, job_title, business_phone, home_phone, mobile_phone, fax_number, address, city, state_province, zip_postal_code, country_region, web_page, notes, attachments)
    - suppliers (id, company, last_name, first_name, email_address, job_title, business_phone, home_phone, mobile_phone, fax_number, address, city, state_province, zip_postal_code, country_region, web_page, notes, attachments)

    Example questions:
    1. What is the total quantity of products sold?
       Example SQL: SELECT p.product_name, SUM(od.quantity) AS total_quantity_sold 
       FROM order_details od
       JOIN products p ON od.product_id = p.id
       GROUP BY p.product_name;
    2. What is the total sales for the year 2023?
       Example SQL: SELECT SUM(od.unit_price * od.quantity) AS total_sales 
       FROM orders o
       JOIN order_details od ON o.id = od.order_id
       WHERE YEAR(o.shipped_date) = 2023;

    Ensure that all tables and aliases are correctly referenced and that the SQL query is valid.
    """
]

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
        #st.write(f"Tentativa {attempts + 1}: Consulta SQL Gerada:", sql_query)  # Exibir a consulta gerada para depuração
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
