#!/usr/bin/env python
# coding: utf-8

# In[3]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.offline as pyo
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from dash.dependencies import Input, Output

get_ipython().run_line_magic('matplotlib', 'inline')
plt.close('all')


# In[4]:


path_to_file = "C:\\Users\\Kuba\\Desktop\\Stack dane\\survey_results_public.csv"
data = pd.read_csv(path_to_file,encoding = 'utf-8',sep = ',')
print(type(data))


# In[5]:


data.head()


# In[6]:


fig1 = go.Figure(data = [go.Histogram(x=data['Gender'])])
fig1.update_traces(marker_color='rgb(12,44,252)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.7)
fig1.update_layout( title={
        'text': "Płeć",
        'y':0.9,
        'x':0.5,
        'font_size':30,
        'xanchor': 'center',
        'yanchor': 'top'}, 
paper_bgcolor =("Lightblue"))
fig1.show()


# In[7]:


fig2 = go.Figure(data = [go.Histogram(x=data['Age'])])
fig2.update_traces(marker_color='rgb(102,25,0)', marker_line_color='rgb(0,0,0)',
                  marker_line_width=0.2, opacity=0.7)
fig2.update_layout(title={
        'text': "Wiek",
        'y':0.9,
        'x':0.5,
        'font_size':30,
        'xanchor': 'center',
        'yanchor': 'top'},  paper_bgcolor =("Lightblue"))
fig2.show()


# In[8]:


fig3 = go.Figure(data = [go.Histogram(x=data['Hobbyist'])])
fig3.update_traces(marker_color='rgb(114,229,57)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.7)
fig3.update_layout(title={
        'text': "Czy traktujesz programowanie jako hobby",
        'y':0.9,
        'x':0.5,
        'font_size':30,
        'xanchor': 'center',
        'yanchor': 'top'},  paper_bgcolor =("Lightblue"))
fig3.show()


# In[9]:


fig4 = go.Figure(data = [go.Histogram(x=data['MainBranch'])])
#fig4.update_layout(plot_bgcolor = 'rgb(158,202,225)')
fig4.update_traces(marker_color='rgb(62,178,134)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig4.update_layout(title={
        'text': "Czym sie zajmujesz",
        'y':0.9,
        'x':0.5,
        'font_size':30,
        'xanchor': 'center',
        'yanchor': 'top'} , paper_bgcolor =("Lightblue"))

fig4.show()


# In[10]:


fig5 = go.Figure(data = [go.Histogram(x=data['SOVisitFreq'])])
fig5.update_traces(marker_color='rgb(255,50,50)', marker_line_color='rgb(255,0,0)',
                  marker_line_width=1.5, opacity=0.7)
fig5.update_layout(title={
        'text': "Jak często wchodzisz na StackOverflow",
        'y':0.9,
        'x':0.5,
        'font_size':30,
        'xanchor': 'center',
        'yanchor': 'top'},  paper_bgcolor =("Lightblue"))
fig5.show()


# In[11]:


fig6 = go.Figure(data = [go.Histogram(x=data['SOFindAnswer'])])
fig6.update_traces(marker_color='rgb(255,101,50)', marker_line_color='rgb(255,0,0)',
                  marker_line_width=1.5, opacity=0.7)
fig6.update_layout(title={
        'text': "Jak często znajdujesz odpowiedź na StackOverflow",
        'y':0.9,
        'x':0.5,
        'font_size':30,
        'xanchor': 'center',
        'yanchor': 'top'},  paper_bgcolor =("Lightblue"))
fig6.show()


# In[21]:


#test
 
app = dash.Dash()

app.layout = html.Div(children=[html.Div("Analiza ankiet ze StackOverflow",style = {
    "color": "black",
    "background-color": "Lightblue",
    "border-style": "groove",
    "display": "inline-block",
    "width": "100%",
    "height": "50px",
    "text-align": "center",
    "font-size": "45px"
    
}),
                                html.Div([
    dcc.Tabs([
        dcc.Tab(label='Ogólne informacje',style = {'backgroundColor':'Lightblue'}, children=[
                                    html.P(
                                        "\
                                    Celem tej strony jest przedstawienie części wyników ankiet, \
                                    które wypełniali użytkownicy StackOverflow.",
                                        style={"color": "#black"}
                                    ),
            ]),
        dcc.Tab(label='Wykresy',style = {'backgroundColor':'Lightblue'}, children=[
           dcc.Dropdown(id = "drop_down",
    options=[
        {'label': 'Płeć', 'value': 'Gender'},
        {'label': 'Wiek', 'value': 'Age'},
        {'label': 'Hobby', 'value': 'Hobbyist'},
        {'label': 'Praca', 'value': 'MainBranch'},
        {'label': 'Ilość wejść', 'value': 'SOVisitFreq'},
        {'label': 'Ilość znalezionych odp', 'value': 'SOFindAnswer'}
    ],
    multi=True
),
            html.Div(id='output')
        ]),
    ])
])
                                ],style = {"width":"100%",'paffing':10})

@app.callback(
    Output('output','children'),
    [Input('drop_down','value')]
)

def show_charts(selected_chart):
    graphs = []
    for values in selected_chart:
        if values == 'Gender':
            graphs.append(html.Div(dcc.Graph(id = "plot_area1",figure = fig1  ,style = {
                                     "background-color": "Blue"
                                 })))
        if values == 'Age':
            graphs.append(html.Div(dcc.Graph(id = "plot_area2",figure = fig2  ,style = {
                                     "background-color": "Blue"
                                 })))
        if values == 'Hobbyist':
            graphs.append(html.Div(dcc.Graph(id = "plot_area3",figure = fig3  ,style = {
                                     "background-color": "Blue"
                                 })))
        if values == 'MainBranch':
            graphs.append(html.Div(dcc.Graph(id = "plot_area4",figure = fig4  ,style = {
                                     "background-color": "Blue"
                                 })))
        if values == 'SOVisitFreq':
            graphs.append(html.Div(dcc.Graph(id = "plot_area5",figure = fig5  ,style = {
                                     "background-color": "Blue"
                                 })))
        if values == 'SOFindAnswer':
            graphs.append(html.Div(dcc.Graph(id = "plot_area6",figure = fig6  ,style = {
                                     "background-color": "Blue"
                                 })))
    return graphs

if __name__ == '__main__':
    app.run_server()


# In[ ]:




