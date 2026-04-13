import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="jobsdb",
    user="postgres",
    password="password"
)

query = "SELECT title, salary_min, location FROM jobs LIMIT 1000"
df = pd.read_sql(query, conn)

st.title("Job Market Insights")

st.bar_chart(df("salary_min"))
st.dataframe(df)
