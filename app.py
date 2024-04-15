import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('C:\\Users\\Hsaito\\Desktop\\TripleTen\\Sprint 5\\projeto\\PROJETO_5\\vehicles.csv') # lendo os dados
#Criando um cabeçalho
st.header('Atividade de Aprofundamento - Sprint 5')

#Criando um histograma para visualizar a quantidade de carros por kilometragem
hist_button = st.button('Criar histograma') # criar um botão
if hist_button:
    st.write('Criando um histograma para verificar a quantidade de carros de acordo com sua kilometragem')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

#Criando gráfico de cores para visualizar quais são as cores de carro mais populares
color_graph_button = st.button('Criando gráfico de cores')
car_colors = car_data['paint_color'].value_counts()
car_colors_df = car_colors.reset_index()
if color_graph_button: #Criando o botão
    st.write('Criando gráfico de verificação de cores mais populares')
    fig_car_colors = px.bar(car_colors_df, x='paint_color', y='count', title='Número de Carros por Cor', labels={'count':'Número de Carros', 'paint_color':'Cor'})
    st.plotly_chart(fig_car_colors, use_container_width=True)

#Criando histograma relacionando o preço médio de veículos e suas condições
car_data['mean_value_by_condition'] = car_data.groupby(['condition','model'])['price'].transform('mean')
price_by_condition = car_data.groupby('condition')['mean_value_by_condition'].mean().reset_index()
price_by_condition_button = st.button('Histograma Preço x Estado do veículo')
if price_by_condition_button:
    st.write('Criando histograma Preço x Condição do Veículo')
    fig_price_by_condition = px.histogram(price_by_condition, x='condition', y='mean_value_by_condition', title='Valores de carro por tipo',labels={'condition':'Estado do veículo','mean_value_by_condition':'Valor médio em $'})
    st.plotly_chart(fig_price_by_condition, use_container_width=True)

#Criando gráfico de dispersão para verificar a correlação entre o preço e a rodagem do veículo F-150
model_f150 =  car_data[car_data['model'].str.lower() == 'ford f-150']
oddometer_by_price_button = st.button('Gráfico de dispersão Preço x Rodagem')
if oddometer_by_price_button: #criando o botão
    st.write('Criando gráfico de dispersão Preço x Rodagem')
    fig_scatter_price_by_condition = px.scatter(model_f150, x ='price',y='odometer',title='Preço do carro por rodagem', opacity=0.5, labels={'price':'Preço do veículo','odometer':'KM Rodado'})
    st.plotly_chart(fig_scatter_price_by_condition, use_container_width=True)


