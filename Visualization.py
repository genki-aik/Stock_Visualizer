import datetime
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def update_value(input_data):
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.now()

    df = web.DataReader(input_data, 'yahoo', start, end)
    print(df)

    # return dcc.Graph(id ="example",
    #     figure ={
    #         'data':[{'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data},
    #         ],
    #         'layout':{
    #             'title':input_data
    #         }
    #     }
    # )
update_value("Data")

# app = dash.Dash()
# app.title = "Stock Visualization"
# app.layout = html.Div(children =[
#     html.H1("Stock Visualization Dashboard"),

#     html.H4("Please enter the stock name"),

#     dcc.Input(id ='input', value = '', type = 'text'),

#     html.Div(id = 'output-graph')
# ])

#app.run_server()