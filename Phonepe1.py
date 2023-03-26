#import all necessory libraries
import pandas as pd
import streamlit as st
import mysql.connector
import plotly.express as px
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)


st.title("Phone pe Data Analysis")


## Execute the SQL query and store the result in a Pandas dataframe
user = 'root'
password = 'pettaparaak007'
host = 'localhost'
database = 'phone_pe'
raise_on_warnings = True



cnx = mysql.connector.connect(host="localhost", user="root", password="pettaparaak007")
cursor = cnx.cursor()
query = "SELECT * FROM phone_pe.agg_trans"
agg_tran = pd.read_sql(query, cnx) 


#standard state names for graph
agg_tran['State'] = agg_tran['State'].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar Island','andhra-pradesh':'Andhra Pradesh', 'arunachal-pradesh':'Arunanchal Pradesh',
       'assam':'Assam', 'bihar':'Bihar', 'chandigarh':'Chandigarh', 'chhattisgarh':'Chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu':'Dadra and Nagar Haveli and Daman and Diu', 'delhi': 'Delhi', 'goa':'Goa', 'gujarat': 'Gujarat',
       'haryana':'Haryana','himachal-pradesh':'Himachal Pradesh', 'jammu-&-kashmir':'Jammu & Kashmir', 'jharkhand':'Jharkhand',
       'karnataka':'Karnataka', 'kerala':'Kerala', 'ladakh':'Ladakh', 'lakshadweep':'Lakshadweep', 'madhya-pradesh':'Madhya Pradesh',
       'maharashtra':'Maharashtra', 'manipur':'Manipur', 'meghalaya':'Meghalaya', 'mizoram':'Mizoram', 'nagaland':'Nagaland',
       'odisha':'Odisha', 'puducherry':'Puducherry', 'punjab':'Punjab', 'rajasthan':'Rajasthan', 'sikkim':'Sikkim',
       'tamil-nadu': 'Tamil Nadu', 'telangana':'Telangana', 'tripura':'Tripura', 'uttar-pradesh':'Uttar Pradesh',
       'uttarakhand':'Uttarakhand', 'west-bengal':'West Bengal'})


#Indian graph showing transaction data by statewise

st.title(':blue[PhonePe Pulse Data Analysis(2018-2022)]')
st.subheader('States aggregated transactions')

fig= px.choropleth(
agg_tran,
geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
featureidkey='properties.ST_NM',
locations='State',
hover_data=['Transacion_amount'],
color='Transacion_count',
color_continuous_scale='orRd'
)
# Example list of transactions
transactions = [
    ("Transaction 1", 100.0),
    ("Transaction 2", 200.0),
    ("Transaction 3", 50.0),
    ("Transaction 4", 300.0),
    ("Transaction 5", 150.0),
    ("Transaction 6", 75.0),
    ("Transaction 7", 250.0),
    ("Transaction 8", 175.0),
    ("Transaction 9", 80.0),
    ("Transaction 10", 120.0),
    ("Transaction 11", 90.0),
    ("Transaction 12", 180.0)
]

query = "SELECT * FROM phone_pe.top_trans"
agg_user = pd.read_sql(query, cnx) 

# Sort transactions by amount in descending order
sorted_transaction = sorted(transactions, key=lambda t: t[1], reverse=True)

# Get top 10 transactions
top_10_transactions = sorted_transaction[:10]

# Create dropdown menu
selected_transaction = st.selectbox("Select a transaction", [t[0] for t in top_10_transactions])

# Print selected transaction
st.write(f"You selected transaction: {selected_transaction}")


fig.update_geos(fitbounds="locations")
st.plotly_chart(fig)