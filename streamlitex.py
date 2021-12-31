import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

df = pd.read_csv("Data.csv")
st.write("# Delhi covid situation")

with open("images/fig1.png", "rb") as file:
    btn = st.download_button(
        label="Download image for current cases",
        data=file,
        file_name="CurrentCases.png",
        mime="image/png"
    )


Date=st.text_input('Enter new date',"")
NewCases=st.text_input('Enter new cases')
PositivityRate=st.text_input('Enter positivity rate')
Deaths=st.text_input('Enter new deaths')
HomeIsolation=st.text_input('Enter new home isolation')
BedsOccupied=st.text_input('Enter new Beds Occupied')

new_row = {'Date':Date, 'New Cases':NewCases, 'Positivity Rate':PositivityRate, 'Deaths':Deaths, 'Home Isolation':HomeIsolation, 'Beds occupied':BedsOccupied}
#append row to the dataframe
df = df.append(new_row, ignore_index=True)


fig = go.Figure()
#fig1= go.Figure()
fig = make_subplots(rows=2, cols=1)
fig.add_trace(go.Scatter(x=df['Date'], y=df['New Cases'],
                    mode='lines+markers',
                    name='New Cases',line=dict(color='black', width=4)),row=1, col=1)
fig.add_trace(go.Scatter(x=df['Date'], y=df['Beds occupied'],
                    mode='lines+markers',
                    name='Beds occupied'),row=1, col=1)
fig.add_trace(go.Scatter(x=df['Date'], y=df['Home Isolation'],
                    mode='lines+markers',
                    name='Home Isolation'),row=1, col=1)
fig.add_trace(go.Scatter(x=df['Date'], y=df['Positivity Rate'],
                    mode='lines+markers',
                    name='Positivity Rate'),row=2, col=1)
fig.add_trace(go.Scatter(x=df['Date'], y=df['Deaths'],
                    mode='lines+markers', name='Deaths'),row=2, col=1)

fig.update_layout(title='Covid Situation in Delhi (Source: ANI)',title_font_family="Arial Black",
    title_font_color="black",height=800, width=1000)
#fig.show()
#fig.write_image("/content/drive/MyDrive/file.png")
#fig.write_html("/content/drive/MyDrive/file.html")
#fig1.show()



if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/fig2.png")

df.to_csv('Data1.csv', index=False)

with open("images/fig2.png", "rb") as file:
     btn = st.download_button(
             label="Download image for new cases",
             data=file,
             file_name="NewCases.png",
             mime="image/png"
           )