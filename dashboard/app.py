import pandas as pd 
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys
sys.path.append('../src')
import datetime

# Configuration de la page
st.set_page_config(page_title="Visualisation - Lapage", layout="wide")
st.title("Visualisation - Lapage")
st.sidebar.title("Menu")
df_b2b_age = pd.read_csv(r"..\data\data_enrichies\df_b2b_age.csv", index_col='date', parse_dates = ['date'])
mois_dict = {
    'Janvier': 1, 'Février': 2, 'Mars': 3, 'Avril': 4,
    'Mai': 5, 'Juin': 6, 'Juillet': 7, 'Août': 8,
    'Septembre': 9, 'Octobre': 10, 'Novembre': 11, 'Décembre': 12
}
with st.sidebar:
    annee =  st.select_slider("année",options=[2021,2022,2023], value=2021)
    mois = st.selectbox(label='Mois', options=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'])
    df_filtre = df_b2b_age[(df_b2b_age.index.year == annee) & (df_b2b_age.index.month == mois_dict[mois])]

pages = [
]
#lecture du DF

ca = round(df_b2b_age['price'].sum(),0 )
#ca_journalier = df_b2b_age.groupby(pd.Grouper(key='date', freq='D'))['price'].sum().reset_index()
#ca_journalier.rename(columns={"price":"ca"}, inplace=True)
#ca_mensuel = df_b2b_age.groupby(pd.Grouper(key='date', freq='M'))['price'].sum().reset_index()
#ca_mensuel.rename(columns={"price":"ca"}, inplace=True)
#trier par date (inspensable pour les moy mobile)
#ca_journalier = ca_journalier.sort_values('date').reset_index(drop=True)
#moyenne mobile sur 7 jours
#ca_journalier['mm_7j'] = ca_journalier['ca'].rolling(window=7).mean()
#moyenne mobile sur 30 jours 
#ca_journalier['mm_30j'] = ca_journalier['ca'].rolling(window=30).mean()
#kpi 2 nombre transaction 
nb_transaction = round(df_b2b_age['session_id'].nunique(),0 )
#kpi 3 nombre de produits vendu 
nb_client = df_filtre['client_id'].nunique()

#kpi 4 panier moyen 



c1, c2, c3, c4 = st.columns(4)

c1.metric("CA", 
            f"{ca}€",
            )
c2.metric("Nombre de session unique",
            nb_transaction)
c3.metric("Nombres clients par mois ", 
            nb_client)
#c4.metric


fig = go.Figure()
fig.add_trace(go.Scatter(
    x=ca_journalier['date'], 
    y=ca_journalier['ca'],
    mode='lines',
    name='CA Journalier ',
    line=dict(width=0.3, color='gray'),
    hovertemplate = "%{y:,.0f}€"
    ))

fig.add_trace(go.Scatter(
    x=ca_journalier['date'], 
    y=ca_journalier['mm_7j'],
    mode='lines',
    name='Moyenne Mobile 7j',
    line=dict(width=2.5, color='blue'),
    hovertemplate = "%{y:,.0f}€"
    ))

fig.add_trace(go.Scatter(
    x=ca_journalier['date'], 
    y=ca_journalier['mm_30j'],
    mode='lines',
    name='Moyenne Mobile 30j',
    line=dict(width=4.5, color='red'),
    hovertemplate = "%{y:,.0f}€"
    ))
fig.update_layout(
    title="Analyse du CA et Moyennes Mobiles",
    height = 500, 
    yaxis_title="Montant (€)",
    hovermode="x unified",
    separators = ". "
)
st.plotly_chart(fig, width='stretch')
st.dataframe(df_b2b_age)