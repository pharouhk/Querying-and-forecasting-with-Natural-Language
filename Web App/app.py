import dash
import pandas as pd
import pandasql as ps
import json
import requests
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#1B2631',
    'text': '#FFFFFF'
}

#load the data to memory
df = pd.read_csv('gemini_BTCUSD_2020_1min.csv')


app.layout = html.Div(style={'backgroundColor': colors['background']}, children =[
  html.H2(children='Welcome to The Smart Natural Language Query Dashboard',
    style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
  html.Br(),
  html.H5(children='A seamless way of interacting with your data by typing your questions in English', 
    style={
        'textAlign': 'center',
        'color': colors['text']
        }

    ),
  #search box
  html.Br(),
  html.Br(),
  dcc.Input(id='input-1-state', type='text', 
    placeholder='What insights do you want on Bitcoin? e.g. What was the Closing price in June?',
    autoComplete = 'on',
    style={
      "marginRight": "30px",
      "marginLeft": "10px",
      "width": "50%",
      }

    ),

  html.Button(id='submit-button-state', n_clicks=0, children='Submit', style={'color':colors['text']}),
  
  html.Br(),
  html.Br(),
  html.Div(id="output-2"),

  dcc.Graph(
        id='BTC-chart'
    )

])

#develop the reactions to the interactions
@app.callback(Output('BTC-chart', 'figure'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'))
def update_output(n_clicks, input1):
  if n_clicks ==0:
    #This is data that will be shown when the page is first loaded without any user interactions yet
    queried_df = df.iloc[:100, :]
    fig = px.line(queried_df, x="Date", y="Close", title="Bitcoin Closing Price Trend")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
        )
    return fig
      
  else:
      # Process flow: input -> API GW -> model -> sql 

      #uncomment when endpoints are live and lambda function is available
      url = "https://9u91x3ikx4.execute-api.us-east-1.amazonaws.com/Production"
      
      headers = {"Content-Type": "application/json", 'Access-Control-Allow-Origin' : '*'}
      r = requests.request("POST", url, headers=headers, data=input1)
      
      response = json.loads(r.text)
      #this is for basic logging on the console
      print(response)
      if response["Response Type"] == "prediction": #This handles prediction queries from the user
        predictions = response["Response"]
        fig = px.line(y=predictions, title="It is expected that Bitcoin would would reach : {} USD". format(predictions[-1]))
      else: #This handles descriptive queries from the user
        try:#try to use the returned query on the dataframe
          sql_query = response["Response"]
          modified_query = sql_query.replace("<pad> ", "").replace("</s>", "").replace("table", "df").replace("( USD )", "")
          queried_df = ps.sqldf(modified_query)
          #check to see the nature of the output dataframe and visualize accordingly
          if len(queried_df)==1: #plot the output as a bar
            fig = px.bar(queried_df,
              title="This is a visualization of the answer to your query: {}". format(input1))
          else: #plot the output as a line
            fig = px.line(queried_df, y='Close',
              title="This is a visualization of the answer to your query: {}". format(input1))
        except: #return the query and other information to the user
          fig = px.line(x=[1,2,3,4,5], y=[0,0,0,0,0], 
          title="We seem to be unable to extract insights from your question: '{}'. Try another question".format(modified_query))

  fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
  return fig


if __name__ == '__main__':
    app.run_server(debug=True)
