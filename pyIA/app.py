import streamlit as st
import psycopg2
import pandas as pd
import numpy as np

# Gerar dados aleatórios para o gráfico
random_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['ph', 'solids', 'hardness']
)

st.header('Gráfico de Linha Aleatório')
st.line_chart(random_data)

# Defina as informações de conexão
hostname = "dpg-ckonrk41tcps73b8raj0-a.oregon-postgres.render.com"
port = 5432
database = "dashboarddatabase"
username = "dashboardusa"
password = "age085yQwL1W3ZXs2pJS1Tk3QLKxr4LL"

try:
    # Conecte ao banco de dados com SSL
    conn = psycopg2.connect(
        host=hostname,
        port=port,
        database=database,
        user=username,
        password=password,
        sslmode="require",
    )

    cursor = conn.cursor()

    # Execute uma consulta SQL na tabela do banco de dados
    cursor.execute("SELECT * FROM public.water_potability")  # Certifique-se de que a tabela está no esquema "public"

    dados = cursor.fetchall()

    # Exiba os dados em uma tabela Streamlit
    st.header('Tabela de Dados do Banco de Dados')
    df = pd.DataFrame(dados, columns=[desc[0] for desc in cursor.description])
    st.dataframe(df)

    conn.close()

except Exception as e:
    st.error(f"Erro na conexão ao banco de dados: {e}")
