import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("notebooks/vehicles_us.csv")


#crear contenido de la aplicación basada en Streamlit
#encabezado principal
st.title("Ventas de Vehículos en Estados Unidos🚗")
st.subheader("A continuación puedes apreciar nuestro catalogo de vehículos disponibles para la venta")
st.write(df)
#crear casilla de verificación para ver los datos
#encabezado del checkbox
st.subheader('¿Aún no te decides por un vehículo? Te invitamos a comparar según precios, modelos o estado de los vehículos')
check = st.checkbox('Histograma de precios de vehículos')
if check:
    st.write('Histograma de precios de vehículos')
    #histograma de precios
    fig = px.histogram(
        df,
        x='price',                
        color='model',            
        labels={'price': 'Precio', 'model': 'Modelo'},
        nbins = 20  
    )
    st.plotly_chart(fig)
check2 = st.checkbox('Distribución de precios por condición del vehículo')
if check2: 
    st.write('Distribución de precios por condición del vehículo')
    #Dsitribución de precios por condición del vehículo
    fig2 = px.scatter(
        df,
        x='condition',
        y='price',
        title= 'Relación entre condición del vehículo y precio',
        labels={'condition':'Condición', 'price': 'Precio'}
    )
    st.plotly_chart(fig2)

