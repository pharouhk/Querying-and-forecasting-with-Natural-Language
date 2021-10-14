import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
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
    queried_df = df.iloc[:100, :]
    fig = px.line(queried_df, x="Date", y="Close", title="Bitcoin Closing Price Trend")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
        )
    return fig
      
  else:
    try:
      #input > aws endpoint > sql > python logic goes here...
      queried_df = 0 #placed to intentionally trigger the exception for now...
      fig = px.line(queried_df, x="Date", y="Close", 
        title="This is a display of the answer to your query: {}". format(input1))

      fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
        )
      return fig

    except:
      fig = px.line(x=[1,2,3,4,5], y=[0,0,0,0,0], 
        title="We seem to be unable to extract insights from your question: '{}'. Try another question".format(input1))

      fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
        )
      return fig


  

if __name__ == '__main__':
    app.run_server(debug=True)