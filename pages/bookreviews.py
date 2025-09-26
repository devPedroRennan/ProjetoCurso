import streamlit as st
import pandas as pd

#definindo a pagina do streamlit em wide mode por padrao
st.set_page_config(layout="wide")

#definindo os dataframes em variaveis
df_reviews = pd.read_csv("datasets\customer reviews.csv")
df_top100books = pd.read_csv("datasets\Top-100 Trending Books.csv")

#criando uma lista que armazena o nome dos livros
books = df_top100books["book title"].unique()

#criando a caixa de selecao
book = st.sidebar.selectbox("Livro", books)

#criando o filtro
df_books_per_name = df_top100books[df_top100books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

#atributos
book_name = df_books_per_name["book title"].iloc[0]
book_genre = df_books_per_name["genre"].iloc[0]
book_price = f"${df_books_per_name["book price"].iloc[0]}"
book_year = df_books_per_name["year of publication"].iloc[0]
book_rating = df_books_per_name["rating"].iloc[0]

#criando o titulo
st.title(book_name)
st.subheader(book_genre)

#criando as colunas
col1, col2, col3 = st.columns(3)

#criando o titulo com colunas

col1.metric("Preço", book_price)
col2.metric("Nota", book_rating)
col3.metric("Ano", book_year)

#linha divisoria, so pela estetica
st.divider()

#o for que vai escrever as reviews
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])
    message.caption(row[3])