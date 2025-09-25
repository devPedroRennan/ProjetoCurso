import streamlit as st
import pandas as pd
import plotly.express as px

#definindo a pagina do streamlit em wide mode por padrao
st.set_page_config(layout="wide")

#definindo os dataframes em variaveis
df_reviews = pd.read_csv("datasets\customer reviews.csv")
df_top100books = pd.read_csv("datasets\Top-100 Trending Books.csv")

#pegando os valores maximo e minimo de preco dos livros
preco_max = df_top100books["book price"].max()
preco_min = df_top100books["book price"].min()

#criando o slider
preco = st.sidebar.slider('Preço: ', preco_min, preco_max, preco_max)

#fazendo so aparecer livros de acordo com o preco no slider
df_books_per_price = df_top100books[df_top100books["book price"] <= preco]
df_books_per_price

#definindo colunas
col1, col2 = st.columns(2)

#fazendo o grafico de barras da frequencia de ano de publicação
fig = px.bar(df_books_per_price["year of publication"].value_counts())

#fazendo um histograma do preco dos livros
fig2 = px.histogram(df_books_per_price["book price"])

col1.plotly_chart(fig)
col2.plotly_chart(fig2)